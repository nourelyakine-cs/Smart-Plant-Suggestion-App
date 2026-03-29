import { Thermometer, Droplets, Sun, Award } from "lucide-react";

interface PlantCardProps {
  name: string;
  category: string;
  temperature: string;
  water: string;
  sunlight: string;
  matchScore?: number;
  difficulty?: string;
}

const CATEGORY_EMOJIS: Record<string, string> = {
  légume: "🥦",
  aromatique: "🌿",
  fleur: "🌸",
  plante_grasse: "🌵",
  arbre_fruitier: "🍊",
};

const DIFFICULTY_COLORS: Record<string, string> = {
  facile: "bg-green-100 text-green-700",
  moyen: "bg-yellow-100 text-yellow-700",
  difficile: "bg-red-100 text-red-700",
};

const PlantCard = ({ name, category, temperature, water, sunlight, matchScore, difficulty }: PlantCardProps) => {
  const emoji = CATEGORY_EMOJIS[category] || "🌱";
  const diffColor = difficulty ? (DIFFICULTY_COLORS[difficulty] || "bg-gray-100 text-gray-600") : "";

  return (
    <div className="bg-white p-6 rounded-[35px] shadow-[0_20px_50px_rgba(0,0,0,0.10)] flex flex-col items-center text-center transition-all duration-300 hover:-translate-y-2 hover:shadow-[0_30px_60px_rgba(0,0,0,0.15)] relative overflow-hidden">
      {/* Match score badge */}
      {matchScore !== undefined && (
        <div className="absolute top-4 right-4 flex items-center gap-1 bg-[#D8F3DC] text-[#2D402D] text-xs font-bold px-2.5 py-1 rounded-full">
          <Award size={12} />
          {matchScore}%
        </div>
      )}

      {/* Emoji icon */}
      <div className="w-28 h-28 flex items-center justify-center mb-4 bg-[#F1F8E9] rounded-full text-6xl">
        {emoji}
      </div>

      {/* Name */}
      <h3 className="font-inria text-2xl font-bold text-[#2D402D] mb-2 capitalize">{name}</h3>

      {/* Difficulty badge */}
      {difficulty && (
        <span className={`text-xs font-semibold px-3 py-0.5 rounded-full mb-4 ${diffColor}`}>
          {difficulty}
        </span>
      )}

      {/* Stats */}
      <div className="w-full space-y-3 px-2 mt-2">
        <div className="flex items-center gap-3">
          <Thermometer className="text-red-500 shrink-0" size={20} />
          <span className="font-inria text-sm text-[#2D402D] font-medium text-left">{temperature}</span>
        </div>
        <div className="flex items-center gap-3">
          <Droplets className="text-blue-400 fill-blue-400 shrink-0" size={20} />
          <span className="font-inria text-sm text-[#2D402D] font-medium text-left">{water}</span>
        </div>
        <div className="flex items-center gap-3">
          <Sun className="text-yellow-400 fill-yellow-400 shrink-0" size={20} />
          <span className="font-inria text-sm text-[#2D402D] font-medium text-left">{sunlight}</span>
        </div>
      </div>
    </div>
  );
};

export default PlantCard;
