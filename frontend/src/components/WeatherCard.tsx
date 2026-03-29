import { CloudSun, CloudRain, Sun, Wind, Droplets, Thermometer } from "lucide-react";
import type { WeatherData } from "@/pages/Index";

interface WeatherCardProps {
  city: string;
  weatherData: WeatherData | null;
}

const SEASON_META: Record<string, { icon: string; label: string; color: string }> = {
  printemps: { icon: "🌸", label: "Spring", color: "from-[#D8F3DC] to-[#B7D1B7]" },
  été: { icon: "☀️", label: "Summer", color: "from-[#FFF9C4] to-[#F9E07A]" },
  automne: { icon: "🍂", label: "Autumn", color: "from-[#FFE0B2] to-[#FFA726]" },
  hiver: { icon: "❄️", label: "Winter", color: "from-[#E3F2FD] to-[#90CAF9]" },
};

const WeatherCard = ({ city, weatherData }: WeatherCardProps) => {
  const now = new Date();
  const dateStr = now.toLocaleDateString("en-US", {
    weekday: "long", year: "numeric", month: "long", day: "numeric",
  });
  const timeStr = now.toLocaleTimeString("en-US", { hour: "2-digit", minute: "2-digit" });

  const season = weatherData?.season || "printemps";
  const meta = SEASON_META[season] || SEASON_META["printemps"];
  const temp = weatherData?.temperature ?? null;
  const humidity = weatherData?.humidity ?? null;

  const WeatherIcon = () => {
    if (temp === null) return <CloudSun size={110} className="text-[#2D402D]/80" />;
    if (temp > 28) return <Sun size={110} className="text-yellow-500" />;
    if (temp < 10) return <CloudRain size={110} className="text-blue-400" />;
    return <CloudSun size={110} className="text-[#2D402D]/80" />;
  };

  return (
    <div className={`w-full bg-gradient-to-b ${meta.color} rounded-[32px] p-8 text-[#2D402D] shadow-lg font-inria relative overflow-hidden`}>
      {/* Header row */}
      <div className="flex justify-between items-start mb-4 relative z-10">
        <div>
          <h2 className="text-3xl font-bold capitalize">{weatherData?.city || city}</h2>
          <p className="opacity-70 text-sm">{dateStr}</p>
          {weatherData?.simulated && (
            <span className="text-xs bg-[#2D402D]/10 px-2 py-0.5 rounded-full mt-1 inline-block">
              Estimated data
            </span>
          )}
        </div>
        <div className="text-right">
          <p className="text-xl font-bold">{timeStr}</p>
          <p className="opacity-70 text-sm">{meta.icon} {meta.label}</p>
        </div>
      </div>

      {/* Big weather icon */}
      <div className="flex justify-center my-4 relative z-10">
        <WeatherIcon />
      </div>

      {/* Title */}
      <div className="flex items-center gap-2 mb-6 relative z-10">
        <Wind size={28} />
        <span className="text-3xl font-bold tracking-tight">Weather Analysis</span>
      </div>

      <hr className="border-[#2D402D]/20 mb-6 relative z-10" />

      {/* Stats */}
      <div className="flex flex-wrap lg:flex-nowrap justify-between items-center gap-6 relative z-10">
        {/* Temperature */}
        <div className="flex items-center gap-4 border-r border-[#2D402D]/20 pr-6 shrink-0">
          <Thermometer size={36} className="text-red-500" />
          <div>
            <p className="text-5xl font-bold">{temp !== null ? `${temp}°` : "--"}</p>
            <p className="text-sm opacity-70 font-bold">Temperature (°C)</p>
          </div>
        </div>

        {/* Humidity */}
        <div className="flex items-center gap-4 border-r border-[#2D402D]/20 pr-6 shrink-0">
          <Droplets size={36} className="text-blue-500" />
          <div>
            <p className="text-4xl font-bold">{humidity !== null ? `${humidity}%` : "--"}</p>
            <p className="text-sm opacity-70 font-bold">Humidity</p>
          </div>
        </div>

        {/* Season */}
        <div className="flex items-center gap-3">
          <span className="text-5xl">{meta.icon}</span>
          <div>
            <p className="text-2xl font-bold">{meta.label}</p>
            <p className="text-sm opacity-70">Current season</p>
          </div>
        </div>
      </div>
    </div>
  );
};

export default WeatherCard;
