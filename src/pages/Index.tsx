import { useState } from "react";
import Header from "@/components/Header";
import Hero from "@/components/Hero";
import WhyChoose from "@/components/WhyChoose";
import Categories from "@/components/Categories";
import AIAnalysis from "@/components/AIAnalysis";
import StatsCards from "@/components/StatsCards";
import WeatherCard from "@/components/WeatherCard";
import ChatBot from "@/components/ChatBot";
import Footer from "@/components/Footer";

const Index = () => {
  const [showResults, setShowResults] = useState(false);

  const [cityName, setCityName] = useState("");

  const handleProcessRecommendations = (selectedCity: string) => {
    setCityName(selectedCity);

    setShowResults(true);

    setTimeout(() => {
      const weatherSection = document.getElementById("results-area");
      if (weatherSection) {
        weatherSection.scrollIntoView({ behavior: "smooth" });
      }
    }, 100);
  };

  return (
    <div className="min-h-screen bg-[#F1F8E9] relative flex flex-col scroll-smooth">
      <Header />

      <main className="flex-grow">
        <div id="home">
          <Hero onSearch={handleProcessRecommendations} />
        </div>

        <div id="about">
          <WhyChoose />
        </div>

        {showResults && (
          <div
            id="results-area"
            className="container mx-auto px-6 space-y-24 pb-24 animate-in fade-in slide-in-from-bottom-10 duration-1000"
          >
            <div id="weather" className="scroll-mt-24">
              <WeatherCard city={cityName} />
            </div>

            <div id="plants" className="scroll-mt-24">
              <Categories />
            </div>

            <div className="space-y-12">
              <AIAnalysis city={cityName} />

              <StatsCards />
            </div>
          </div>
        )}
      </main>

      <Footer />

      <div
        id="ai-assistant"
        className="absolute bottom-0 h-1 w-1 opacity-0 pointer-events-none"
      />
      <ChatBot />
    </div>
  );
};

export default Index;
