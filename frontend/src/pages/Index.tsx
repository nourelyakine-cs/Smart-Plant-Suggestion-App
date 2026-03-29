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

const API_URL = import.meta.env.VITE_BACKEND_URL || "http://localhost:8000";

export interface WeatherData {
  city: string;
  temperature: number;
  humidity: number;
  season: string;
  simulated?: boolean;
}

export interface PlantData {
  key: string;
  name: string;
  scientific_name: string;
  category: string;
  difficulty: string;
  water_needs: string;
  sun_needs: string;
  seasons: string[];
  temp_min: number;
  temp_max: number;
  temp_optimal: number[];
  description: string;
  care_tips: string[];
  match_score: number;
}

export interface SuggestionsData {
  city: string;
  weather: WeatherData;
  plants: PlantData[];
  total_matched: number;
  showing: number;
}

const Index = () => {
  const [showResults, setShowResults] = useState(false);
  const [cityName, setCityName] = useState("");
  const [isLoading, setIsLoading] = useState(false);
  const [weatherData, setWeatherData] = useState<WeatherData | null>(null);
  const [suggestionsData, setSuggestionsData] = useState<SuggestionsData | null>(null);
  const [error, setError] = useState<string | null>(null);

  const handleProcessRecommendations = async (selectedCity: string) => {
    setCityName(selectedCity);
    setIsLoading(true);
    setError(null);
    setShowResults(false);

    try {
      const res = await fetch(
        `${API_URL}/api/suggest?city=${encodeURIComponent(selectedCity)}`
      );

      if (!res.ok) {
        const errData = await res.json().catch(() => ({}));
        throw new Error(errData.detail || `Server error (${res.status})`);
      }

      const data: SuggestionsData = await res.json();
      setWeatherData(data.weather);
      setSuggestionsData(data);
      setShowResults(true);

      setTimeout(() => {
        const el = document.getElementById("results-area");
        if (el) el.scrollIntoView({ behavior: "smooth" });
      }, 100);
    } catch (err: any) {
      const msg = err.message || "";
      setError(
        msg.toLowerCase().includes("fetch") || msg.toLowerCase().includes("connect")
          ? "❌ Cannot connect to the backend. Make sure both servers are running (see instructions below)."
          : `❌ ${msg}`
      );
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <div className="min-h-screen bg-[#F1F8E9] relative flex flex-col scroll-smooth">
      <Header />

      <main className="flex-grow">
        <div id="home">
          <Hero onSearch={handleProcessRecommendations} isLoading={isLoading} />
        </div>

        <div id="about">
          <WhyChoose />
        </div>

        {error && (
          <div className="container mx-auto px-6 py-4">
            <div className="bg-red-50 border border-red-200 text-red-700 px-6 py-4 rounded-2xl text-center font-inria text-sm">
              {error}
              <p className="mt-2 text-xs opacity-75">
                1) Run <code className="bg-red-100 px-1 rounded">cd ai && python api/ai_endpoints.py</code> in one terminal
                <br />
                2) Run <code className="bg-red-100 px-1 rounded">cd backend && uvicorn main:app --reload --port 8000</code> in another
              </p>
            </div>
          </div>
        )}

        {showResults && suggestionsData && (
          <div
            id="results-area"
            className="container mx-auto px-6 space-y-24 pb-24 animate-in fade-in slide-in-from-bottom-10 duration-1000"
          >
            <div id="weather" className="scroll-mt-24">
              <WeatherCard city={cityName} weatherData={weatherData} />
            </div>

            <div id="plants" className="scroll-mt-24">
              <Categories plants={suggestionsData.plants} />
            </div>

            <div className="space-y-12">
              <AIAnalysis
                city={cityName}
                plants={suggestionsData.plants}
                weather={weatherData}
                totalMatched={suggestionsData.total_matched}
              />
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
      <ChatBot apiUrl={API_URL} />
    </div>
  );
};

export default Index;
