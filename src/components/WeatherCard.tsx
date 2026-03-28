import { CloudSun, CloudRain, Sun, Wind } from "lucide-react";

interface WeatherCardProps {
  city: string;
}

const WeatherCard = ({ city }: WeatherCardProps) => {
  const forecast = [
    { day: "Tue", icon: <CloudRain size={20} />, temp: "15°" },
    { day: "Wed", icon: <CloudSun size={20} />, temp: "20°" },
    { day: "Thu", icon: <CloudRain size={20} />, temp: "18°" },
    { day: "Fri", icon: <Sun size={20} />, temp: "35°" },
    { day: "Sat", icon: <Sun size={20} />, temp: "30°" },
    { day: "Sun", icon: <CloudRain size={20} />, temp: "10°" },
  ];

  return (
    <div className="w-full bg-gradient-to-b from-[#D8F3DC] to-[#B7D1B7] rounded-[32px] p-8 text-[#2D402D] shadow-lg font-inria relative overflow-hidden transition-all duration-500">
      <div className="flex justify-between items-start mb-4 relative z-10">
        <div>
          <h2 className="text-3xl font-bold capitalize">
            {city ? city : "Algiers"},
          </h2>
          <p className="opacity-70">March 30, 2026</p>
        </div>
        <div className="text-right">
          <p className="text-xl font-bold">20:25 pm</p>
        </div>
      </div>

      <div className="flex justify-center my-4 relative z-10">
        <CloudSun size={120} className="text-[#2D402D]/80" />
      </div>

      <div className="flex items-center gap-2 mb-6 relative z-10">
        <Wind size={30} />
        <span className="text-3xl font-bold tracking-tight">
          Weather Analysis
        </span>
      </div>

      <hr className="border-[#2D402D]/20 mb-6 relative z-10" />

      <div className="flex flex-wrap lg:flex-nowrap justify-between items-center gap-4 relative z-10">
        <div className="flex items-center gap-4 border-r border-[#2D402D]/20 pr-6 shrink-0">
          <div className="text-center">
            <h1 className="text-5xl font-bold">33°</h1>
            <p className="text-sm font-bold opacity-70">Monday</p>
          </div>
          <div className="text-center">
            <CloudSun size={40} />
            <p className="text-xs mt-1 font-bold">4mph / 67°</p>
          </div>
        </div>

        <div className="flex flex-1 justify-around items-center min-w-[300px]">
          {forecast.map((f, i) => (
            <div
              key={i}
              className={`flex flex-col items-center gap-2 ${i !== forecast.length - 1 ? "border-r border-[#2D402D]/20 pr-4" : ""}`}
            >
              <span className="text-sm opacity-70 font-bold">{f.day}</span>
              <div className="hover:scale-125 transition-transform duration-300 cursor-default">
                {f.icon}
              </div>
              <span className="font-bold">{f.temp}</span>
            </div>
          ))}
        </div>
      </div>
    </div>
  );
};

export default WeatherCard;
