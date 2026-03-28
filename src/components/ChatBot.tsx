import { Send, Bot, X, MessageSquare } from "lucide-react";
import { useState, useEffect } from "react";

const ChatBot = () => {
  const [isOpen, setIsOpen] = useState(false);

  useEffect(() => {
    const handleOpenChat = () => {
      setIsOpen(true);
      window.scrollTo({
        top: document.documentElement.scrollHeight,
        behavior: "smooth",
      });
    };

    window.addEventListener("openChat", handleOpenChat);

    return () => window.removeEventListener("openChat", handleOpenChat);
  }, []);

  return (
    <div className="fixed top-0 left-0 w-full h-full pointer-events-none z-[99999] font-inria">
      {!isOpen && (
        <button
          onClick={() => setIsOpen(true)}
          className="absolute bottom-10 right-10 pointer-events-auto bg-[#2D402D] text-white p-4 rounded-full shadow-2xl hover:scale-110 transition-all border-2 border-white/20 flex items-center justify-center w-16 h-16"
        >
          <MessageSquare size={30} />
        </button>
      )}

      {isOpen && (
        <div className="absolute bottom-10 right-10 pointer-events-auto bg-white w-[350px] md:w-[380px] h-[520px] rounded-[35px] shadow-[0_20px_50px_rgba(0,0,0,0.2)] border border-gray-100 overflow-hidden flex flex-col animate-in slide-in-from-bottom-5 duration-300">
          {/* Header */}
          <div className="bg-[#D8F3DC] p-6 flex justify-between items-center">
            <div className="flex items-center gap-3">
              <div className="bg-white/80 p-2 rounded-xl">
                <Bot size={22} className="text-[#2D402D]" />
              </div>
              <span className="font-bold text-[#2D402D] text-lg">
                GreenGuide AI
              </span>
            </div>
            <button
              onClick={() => setIsOpen(false)}
              className="text-[#2D402D]/50 hover:text-[#2D402D]"
            >
              <X size={24} />
            </button>
          </div>

          <div className="flex-1 p-6 overflow-y-auto bg-white">
            <div className="bg-[#F5F5F5] p-5 rounded-[25px] rounded-tl-none text-[#2D402D] leading-relaxed">
              <p className="font-bold mb-2">Hello! 🌿</p>
              <p className="text-sm opacity-90">
                I'm your GreenGuide AI assistant. I can help you find plants and
                give care tips!
              </p>
            </div>
          </div>

          <div className="p-5 bg-white border-t border-gray-50">
            <div className="relative flex items-center bg-gray-50 border border-gray-200 rounded-full px-4 py-1 focus-within:bg-white focus-within:ring-2 focus-within:ring-[#D8F3DC] transition-all">
              <input
                type="text"
                placeholder="Ask me anything..."
                className="flex-1 bg-transparent border-none focus:ring-0 text-[14px] py-3 text-gray-700 outline-none"
              />
              <button className="bg-[#D8F3DC] text-[#2D402D] p-2.5 rounded-full hover:bg-[#2D402D] hover:text-white transition-all">
                <Send size={18} />
              </button>
            </div>
          </div>
        </div>
      )}
    </div>
  );
};

export default ChatBot;
