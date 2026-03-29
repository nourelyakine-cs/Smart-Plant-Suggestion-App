import { Send, Bot, X, MessageSquare, Loader2, Trash2 } from "lucide-react";
import { useState, useEffect, useRef } from "react";

interface Message {
  role: "user" | "bot";
  text: string;
  timestamp: string;
}

interface ChatBotProps {
  apiUrl?: string;
}

const SESSION_ID = `session_${Date.now()}`;

const ChatBot = ({ apiUrl = "http://localhost:8000" }: ChatBotProps) => {
  const [isOpen, setIsOpen] = useState(false);
  const [messages, setMessages] = useState<Message[]>([
    {
      role: "bot",
      text: "Hello! 🌿 I'm your GreenGuide AI assistant. I can help you find the best plants for your location and give personalized care tips!\n\nTry asking: *\"What plants grow well in Paris?\"* or *\"Tips for my tomatoes?\"*",
      timestamp: new Date().toLocaleTimeString(),
    },
  ]);
  const [input, setInput] = useState("");
  const [isLoading, setIsLoading] = useState(false);
  const messagesEndRef = useRef<HTMLDivElement>(null);
  const inputRef = useRef<HTMLInputElement>(null);

  // Auto-open via custom event (from nav links etc)
  useEffect(() => {
    const handler = () => setIsOpen(true);
    window.addEventListener("openChat", handler);
    return () => window.removeEventListener("openChat", handler);
  }, []);

  // Scroll to bottom on new message
  useEffect(() => {
    messagesEndRef.current?.scrollIntoView({ behavior: "smooth" });
  }, [messages, isLoading]);

  // Focus input when chat opens
  useEffect(() => {
    if (isOpen) setTimeout(() => inputRef.current?.focus(), 300);
  }, [isOpen]);

  const sendMessage = async () => {
    const text = input.trim();
    if (!text || isLoading) return;

    setInput("");
    const userMsg: Message = { role: "user", text, timestamp: new Date().toLocaleTimeString() };
    setMessages((prev) => [...prev, userMsg]);
    setIsLoading(true);

    try {
      const res = await fetch(`${apiUrl}/api/chat`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ message: text, session_id: SESSION_ID }),
      });

      const data = await res.json();

      const botText = data.response ||
        (data.success === false ? data.response || data.error : null) ||
        "Sorry, I couldn't process your request. Please try again.";

      setMessages((prev) => [
        ...prev,
        { role: "bot", text: botText, timestamp: new Date().toLocaleTimeString() },
      ]);
    } catch {
      setMessages((prev) => [
        ...prev,
        {
          role: "bot",
          text: "⚠️ Cannot reach the AI service. Make sure the backend servers are running.",
          timestamp: new Date().toLocaleTimeString(),
        },
      ]);
    } finally {
      setIsLoading(false);
    }
  };

  const clearChat = async () => {
    try {
      await fetch(`${apiUrl}/api/chat`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ message: "__clear__", session_id: SESSION_ID }),
      }).catch(() => {});
    } catch {}
    setMessages([
      {
        role: "bot",
        text: "Chat cleared! 🌿 How can I help you with your garden?",
        timestamp: new Date().toLocaleTimeString(),
      },
    ]);
  };

  const handleKeyDown = (e: React.KeyboardEvent) => {
    if (e.key === "Enter" && !e.shiftKey) {
      e.preventDefault();
      sendMessage();
    }
  };

  return (
    <div className="fixed top-0 left-0 w-full h-full pointer-events-none z-[99999] font-inria">
      {/* Toggle button */}
      {!isOpen && (
        <button
          onClick={() => setIsOpen(true)}
          className="absolute bottom-8 right-8 pointer-events-auto bg-[#2D402D] text-white p-4 rounded-full shadow-2xl hover:scale-110 active:scale-95 transition-all border-2 border-white/20 flex items-center justify-center w-16 h-16"
          aria-label="Open chat"
        >
          <MessageSquare size={28} />
        </button>
      )}

      {/* Chat window */}
      {isOpen && (
        <div className="absolute bottom-8 right-8 pointer-events-auto bg-white w-[370px] md:w-[400px] h-[560px] rounded-[32px] shadow-[0_20px_60px_rgba(0,0,0,0.25)] border border-gray-100 overflow-hidden flex flex-col animate-in slide-in-from-bottom-5 duration-300">
          {/* Header */}
          <div className="bg-[#2D402D] px-6 py-4 flex justify-between items-center shrink-0">
            <div className="flex items-center gap-3">
              <div className="bg-white/15 p-2 rounded-xl">
                <Bot size={22} className="text-white" />
              </div>
              <div>
                <span className="font-bold text-white text-base block">GreenGuide AI</span>
                <span className="text-white/60 text-xs">Plant Expert Assistant</span>
              </div>
            </div>
            <div className="flex items-center gap-2">
              <button
                onClick={clearChat}
                className="text-white/40 hover:text-white/80 transition-colors p-1.5 rounded-lg hover:bg-white/10"
                title="Clear chat"
              >
                <Trash2 size={16} />
              </button>
              <button
                onClick={() => setIsOpen(false)}
                className="text-white/40 hover:text-white transition-colors p-1.5 rounded-lg hover:bg-white/10"
              >
                <X size={20} />
              </button>
            </div>
          </div>

          {/* Messages area */}
          <div className="flex-1 overflow-y-auto p-4 space-y-3 bg-[#F9FFF9]">
            {messages.map((msg, i) => (
              <div key={i} className={`flex ${msg.role === "user" ? "justify-end" : "justify-start"}`}>
                <div
                  className={`max-w-[85%] rounded-2xl px-4 py-3 text-sm leading-relaxed whitespace-pre-wrap ${
                    msg.role === "user"
                      ? "bg-[#2D402D] text-white rounded-br-sm"
                      : "bg-white text-[#2D402D] border border-[#2D402D]/10 rounded-bl-sm shadow-sm"
                  }`}
                >
                  {msg.text}
                  <p className={`text-[10px] mt-1.5 ${msg.role === "user" ? "text-white/50" : "text-[#2D402D]/30"}`}>
                    {msg.timestamp}
                  </p>
                </div>
              </div>
            ))}

            {/* Loading indicator */}
            {isLoading && (
              <div className="flex justify-start">
                <div className="bg-white border border-[#2D402D]/10 rounded-2xl rounded-bl-sm px-4 py-3 shadow-sm flex items-center gap-2">
                  <Loader2 size={16} className="animate-spin text-[#2D402D]" />
                  <span className="text-sm text-[#2D402D]/60">Thinking...</span>
                </div>
              </div>
            )}
            <div ref={messagesEndRef} />
          </div>

          {/* Input bar */}
          <div className="px-4 py-3 bg-white border-t border-gray-100 shrink-0">
            <div className="flex items-center gap-2 bg-[#F1F8E9] border border-[#2D402D]/15 rounded-2xl px-4 py-2 focus-within:border-[#2D402D]/40 focus-within:ring-2 focus-within:ring-[#D8F3DC] transition-all">
              <input
                ref={inputRef}
                type="text"
                value={input}
                onChange={(e) => setInput(e.target.value)}
                onKeyDown={handleKeyDown}
                placeholder="Ask about plants..."
                disabled={isLoading}
                className="flex-1 bg-transparent border-none focus:ring-0 text-sm py-1.5 text-[#2D402D] placeholder:text-[#2D402D]/40 outline-none disabled:opacity-50"
              />
              <button
                onClick={sendMessage}
                disabled={isLoading || !input.trim()}
                className="bg-[#2D402D] text-white p-2 rounded-xl hover:bg-[#1b2b1b] active:scale-95 transition-all disabled:opacity-40 disabled:cursor-not-allowed"
              >
                <Send size={16} />
              </button>
            </div>
          </div>
        </div>
      )}
    </div>
  );
};

export default ChatBot;
