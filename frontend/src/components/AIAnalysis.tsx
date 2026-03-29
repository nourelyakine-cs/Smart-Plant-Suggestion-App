import { Sparkles, CheckCircle2, Leaf, Thermometer, Award } from "lucide-react";
import type { PlantData, WeatherData } from "@/pages/Index";

const SEASON_LABELS: Record<string, string> = {
  printemps: "🌸 Spring — Perfect for starting seeds",
  été: "☀️ Summer — Great for heat-loving plants",
  automne: "🍂 Autumn — Ideal for root vegetables",
  hiver: "❄️ Winter — Focus on cold-hardy plants",
};

interface AIAnalysisProps {
  city?: string;
  plants?: PlantData[];
  weather?: WeatherData | null;
  totalMatched?: number;
}

const AIAnalysis = ({ city, plants = [], weather, totalMatched = 0 }: AIAnalysisProps) => {
  const topPlant = plants[0];
  const seasonTip = weather ? (SEASON_LABELS[weather.season] || weather.season) : null;

  return (
    <div className="bg-[#F9FFF9] border border-[#2D402D]/20 rounded-[40px] p-8 mb-16 shadow-sm max-w-5xl mx-auto animate-in fade-in duration-700">
      <div className="flex items-center gap-3 mb-6">
        <div className="bg-white p-2 rounded-xl shadow-sm border border-[#2D402D]/10">
          <Sparkles className="text-[#2D402D]" size={28} />
        </div>
        <h2 className="font-inria text-3xl font-bold text-[#2D402D]">
          AI Analysis for <span className="capitalize">{city || "your location"}</span>:
        </h2>
      </div>

      <div className="space-y-4 ml-2">
        {/* Matched count */}
        <div className="flex items-center gap-3 text-lg font-inria text-[#2D402D]">
          <CheckCircle2 className="text-green-600 shrink-0" size={20} />
          <p>
            Analyzed <strong>{totalMatched}</strong> plants against current weather in{" "}
            <span className="font-bold capitalize">{city || "this area"}</span>.
            Showing top <strong>{plants.length}</strong>.
          </p>
        </div>

        {/* Top recommendation */}
        {topPlant && (
          <div className="flex items-start gap-3">
            <Award className="text-[#8B9D44] shrink-0 mt-0.5" size={20} />
            <p className="text-lg font-inria text-[#2D402D] italic font-medium">
              🏆 Top recommendation:{" "}
              <strong>{topPlant.name}</strong> with a{" "}
              <strong>{topPlant.match_score}% match</strong> — {topPlant.description}
            </p>
          </div>
        )}

        {/* Temperature info */}
        {weather && (
          <div className="flex items-center gap-3">
            <Thermometer className="text-red-500 shrink-0" size={20} />
            <p className="text-lg font-inria text-[#2D402D] italic font-medium">
              🌡️ Current temperature: <strong>{weather.temperature}°C</strong>,
              humidity: <strong>{weather.humidity}%</strong>
            </p>
          </div>
        )}

        {/* Season tip */}
        {seasonTip && (
          <div className="flex items-center gap-3">
            <Leaf className="text-[#2D402D] shrink-0" size={20} />
            <p className="text-lg font-inria text-[#2D402D] italic font-medium">
              {seasonTip}
            </p>
          </div>
        )}
      </div>
    </div>
  );
};

export default AIAnalysis;