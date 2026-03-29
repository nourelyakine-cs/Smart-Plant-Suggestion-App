import { Leaf } from "lucide-react";

const Header = () => {
  const scrollToSection = (id: string) => {
    const element = document.getElementById(id);
    if (element) {
      element.scrollIntoView({ behavior: "smooth" });
    }
  };

  return (
    <>
      <div className="w-full flex items-center justify-center py-6 md:py-10 bg-white"> 
        <Leaf className="text-leaf mr-2 md:mr-3" size={28} md-size={36} /> 
        <span className="font-display text-2xl md:text-4xl font-extrabold tracking-tighter text-foreground">
          <span className="text-olive">GREEN</span>
          <span className="text-leaf">GUIDE</span>
        </span>
      </div>

      <nav className="sticky top-0 z-[100] w-full bg-white/90 backdrop-blur-md shadow-sm border-b border-border/40">
        <div className="container mx-auto py-3 px-4">
          <ul className="flex flex-wrap items-center justify-center gap-x-4 gap-y-2 md:gap-14 text-[10px] md:text-sm font-bold text-foreground/80"> 
            <li>
              <button 
                onClick={() => scrollToSection('home')} 
                className="hover:text-olive transition-all uppercase tracking-widest px-2 py-1"
              >
                HOME
              </button>
            </li>
            <li>
              <button 
                onClick={() => scrollToSection('about')} 
                className="hover:text-olive transition-all uppercase tracking-widest px-2 py-1"
              >
                About
              </button>
            </li>
            <li>
              <button 
                onClick={() => scrollToSection('weather')} 
                className="hover:text-olive transition-all uppercase tracking-widest px-2 py-1 text-center"
              >
                Weather <span className="hidden md:inline">Analysis</span>
              </button>
            </li>
            <li>
              <button 
                onClick={() => scrollToSection('plants')} 
                className="hover:text-olive transition-all uppercase tracking-widest px-2 py-1 text-center"
              >
                <span className="hidden md:inline">Explore</span> Plants
              </button>
            </li>
          </ul>
        </div>
      </nav>
    </>
  );
};

export default Header;
