import { Facebook, Instagram, Linkedin } from "lucide-react";

const Footer = () => {
  const scrollToSection = (id: string) => {
    if (id === "ai-assistant") {
      const event = new CustomEvent("openChat");
      window.dispatchEvent(event);
    } else {
      const element = document.getElementById(id);
      if (element) {
        element.scrollIntoView({ behavior: "smooth" });
      }
    }
  };

  return (
    <footer className="bg-[#A7B29F] py-16 px-6 mt-20 border-t border-[#2D402D]/10">
      <div className="container mx-auto grid grid-cols-1 md:grid-cols-3 gap-12 text-[#2D402D]">
        <div className="flex flex-col gap-5">
          <div className="flex items-center gap-3">
            <svg
              width="45"
              height="45"
              viewBox="0 0 100 100"
              fill="none"
              xmlns="http://www.w3.org/2000/svg"
            >
              <path
                d="M80,20 C50,20 20,50 20,80 C20,80 50,80 80,50 C80,50 80,20 80,20 Z M50,50 L20,80"
                stroke="#2D402D"
                strokeWidth="5"
                fill="#6B8E23"
              />
            </svg>
            <h2 className="text-3xl font-serif font-bold tracking-tighter uppercase text-[#2D402D]">
              GREENGUIDE
            </h2>
          </div>
          <p className="text-lg leading-relaxed max-w-[300px] font-serif opacity-90">
            Helping you choose the right plants the smart way.
          </p>
        </div>

        <div className="flex flex-col gap-5">
          <h4 className="text-xl font-bold font-serif uppercase tracking-wider">
            Navigation
          </h4>
          <nav className="flex flex-col gap-3 uppercase text-sm font-bold">
            <button
              onClick={() => scrollToSection("home")}
              className="text-left hover:text-white transition-colors uppercase"
            >
              HOME
            </button>
            <button
              onClick={() => scrollToSection("about")}
              className="text-left hover:text-white transition-colors uppercase"
            >
              About
            </button>
            <button
              onClick={() => scrollToSection("plants")}
              className="text-left hover:text-white transition-colors uppercase"
            >
              Explore plants
            </button>
            <button
              onClick={() => scrollToSection("weather")}
              className="text-left hover:text-white transition-colors uppercase"
            >
              Weather Analysis
            </button>

            <button
              onClick={() => scrollToSection("ai-assistant")}
              className="text-left hover:text-white transition-colors uppercase"
            >
              AI Assistant
            </button>
          </nav>
        </div>

        <div className="flex flex-col gap-5">
          <h4 className="text-xl font-bold font-serif uppercase tracking-wider">
            Information
          </h4>
          <div className="flex flex-col gap-3 text-md font-serif">
            <span className="font-bold">+213567478930</span>
            <a href="mailto:Greenguidell@gmail.com" className="hover:underline">
              Greenguidell@gmail.com
            </a>
            <span>450, Alger, Algiers.</span>
          </div>
        </div>
      </div>

      <div className="container mx-auto mt-20 pt-10 border-t border-[#2D402D]/20 flex flex-col items-center gap-8">
        <p className="text-center font-serif italic text-xl text-[#2D402D]">
          All rights reserved | Made for smarter and greener living.
        </p>

        <div className="flex gap-5">
          <a
            href="#"
            className="w-12 h-12 bg-black text-white rounded-full flex items-center justify-center hover:scale-110 transition-transform shadow-xl"
          >
            <Facebook size={22} fill="currentColor" />
          </a>
          <a
            href="#"
            className="w-12 h-12 bg-black text-white rounded-full flex items-center justify-center hover:scale-110 transition-transform shadow-xl"
          >
            <Instagram size={22} />
          </a>
          <a
            href="#"
            className="w-12 h-12 bg-black text-white rounded-full flex items-center justify-center hover:scale-110 transition-transform shadow-xl"
          >
            <Linkedin size={22} fill="currentColor" />
          </a>
          <a
            href="#"
            className="w-12 h-12 bg-black text-white rounded-full flex items-center justify-center hover:scale-110 transition-transform shadow-xl font-bold text-2xl font-serif"
          >
            X
          </a>
        </div>
      </div>
    </footer>
  );
};

export default Footer;
