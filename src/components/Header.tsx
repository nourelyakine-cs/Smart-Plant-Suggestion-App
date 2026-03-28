import { Leaf } from "lucide-react";

const Header = () => {
  const scrollToSection = (id: string) => {
    const element = document.getElementById(id);
    if (element) {
      element.scrollIntoView({ behavior: "smooth" });
    }
  };

  return (
    <header className="w-full bg-white/70 backdrop-blur-md sticky top-0 z-50 border-b border-border/40">
      
      <div className="flex items-center justify-center py-8"> 
        <Leaf className="text-leaf mr-3" size={40} /> 
        <span className="font-display text-4xl font-extrabold tracking-tighter text-foreground">
          <span className="text-olive">GREEN</span>
          <span className="text-leaf">GUIDE</span>
        </span>
      </div>

      <nav className="border-t border-border/50 bg-white/30">
        <div className="container mx-auto flex items-center justify-center py-5 px-6">
          <ul className="flex items-center gap-16 text-lg font-bold text-foreground/80"> 
            <li>
              <button 
                onClick={() => scrollToSection('home')} 
                className="hover:text-olive transition-all hover:scale-110 uppercase tracking-widest"
              >
                HOME
              </button>
            </li>
            <li>
              <button 
                onClick={() => scrollToSection('about')} 
                className="hover:text-olive transition-all hover:scale-110 uppercase tracking-widest"
              >
                About
              </button>
            </li>
            <li>
              <button 
                onClick={() => scrollToSection('weather')} 
                className="hover:text-olive transition-all hover:scale-110 uppercase tracking-widest"
              >
                Weather Analysis
              </button>
            </li>
            <li>
              <button 
                onClick={() => scrollToSection('plants')} 
                className="hover:text-olive transition-all hover:scale-110 uppercase tracking-widest"
              >
                Explore Plants
              </button>
            </li>
          </ul>
        </div>
      </nav>
    </header>
  );
};

export default Header;