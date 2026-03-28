import { useState } from "react";
import { Search, MapPin } from "lucide-react";
import monsteraImg from "@/assets/monstera.png";

const Hero = ({ onSearch }: { onSearch: (city: string) => void }) => {
  const [cityInput, setCityInput] = useState("");

  const handleButtonClick = () => {
    if (cityInput.trim() !== "") {
      onSearch(cityInput);
    } else {
      alert("Please enter a city name first! 🌿");
    }
  };

  return (
    <section className="relative bg-background min-h-[85vh] flex items-center pt-32 pb-20 overflow-hidden">
      <div className="absolute top-[-10%] right-[-5%] w-[500px] h-[500px] bg-[#8B9D44]/10 blur-[120px] rounded-full pointer-events-none" />
      <div className="absolute bottom-[-10%] left-[-5%] w-[400px] h-[400px] bg-[#2D402D]/5 blur-[100px] rounded-full pointer-events-none" />

      <div className="container mx-auto px-6 relative z-10">
        <div className="grid grid-cols-1 lg:grid-cols-2 gap-12 lg:gap-20 items-center">
          <div className="flex flex-col space-y-10 text-center lg:text-left items-center lg:items-start">
            <div className="space-y-6">
              <h1
                className="font-inria font-bold text-[#2D402D] leading-[1.1] tracking-tight"
                style={{ fontSize: "clamp(40px, 5vw, 64px)" }}
              >
                Empowering <br />
                <span className="text-[#8B9D44]">Green Cities</span> <br />
                <span className="relative">
                  with AI Intelligence
                  <span className="absolute -bottom-2 left-0 w-1/3 h-1 bg-[#8B9D44]/30 rounded-full hidden lg:block"></span>
                </span>
              </h1>

              <p
                className="font-inria text-[#556B55] max-w-xl leading-relaxed"
                style={{ fontSize: "clamp(18px, 2vw, 24px)" }}
              >
                Optimize your urban garden using real-time weather data and AI
                analysis. GreenGuide helps you choose the most resilient plants
                for your specific location. 🌱
              </p>
            </div>

            <div className="w-full max-w-xl group">
              <div className="flex flex-col sm:flex-row items-center gap-3 bg-white border-2 border-[#2D402D]/10 p-2.5 rounded-[28px] shadow-[0_20px_50px_rgba(45,64,45,0.08)] transition-all duration-300 focus-within:border-[#8B9D44]/40 focus-within:shadow-[0_20px_60px_rgba(139,157,68,0.15)]">
                <div className="relative flex-1 w-full">
                  <MapPin
                    className="absolute left-4 top-1/2 -translate-y-1/2 text-[#2D402D]/30 group-focus-within:text-[#8B9D44]"
                    size={22}
                  />
                  <input
                    type="text"
                    value={cityInput}
                    onChange={(e) => setCityInput(e.target.value)}
                    placeholder="Enter your city (e.g. Algiers)..."
                    className="w-full h-14 pl-12 pr-4 text-lg bg-transparent border-none focus:ring-0 text-[#2D402D] placeholder:text-[#2D402D]/30 font-inria font-medium"
                  />
                </div>

                <button
                  onClick={handleButtonClick}
                  className="bg-[#2D402D] hover:bg-[#1b2b1b] text-white px-8 h-14 rounded-[22px] font-inria font-bold text-lg transition-all duration-300 active:scale-95 flex items-center justify-center gap-2 shadow-lg shadow-[#2D402D]/20 w-full sm:w-auto"
                >
                  <Search size={20} />
                  Get recommendations
                </button>
              </div>
            </div>
          </div>

          <div className="relative flex justify-center lg:justify-end items-center">
            <div className="absolute w-[80%] h-[80%] bg-[#8B9D44]/20 blur-[100px] rounded-full animate-pulse" />
            <img
              src={monsteraImg}
              alt="Monstera Deliciosa"
              className="relative z-10 w-full max-w-[600px] drop-shadow-[0_35px_65px_rgba(0,0,0,0.15)] animate-float transition-transform duration-700 hover:scale-105"
            />
          </div>
        </div>
      </div>
    </section>
  );
};

export default Hero;
