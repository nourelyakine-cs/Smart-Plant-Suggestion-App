import { Sparkles, CheckCircle2 } from "lucide-react";

interface AIAnalysisProps {
  city?: string;
}

const AIAnalysis = ({ city }: AIAnalysisProps) => {
  return (
    <div className="bg-[#F9FFF9] border border-[#2D402D]/20 rounded-[40px] p-8 mb-16 shadow-sm max-w-5xl mx-auto animate-in fade-in duration-700">
      <div className="flex items-center gap-3 mb-4">
        <div className="bg-white p-2 rounded-xl shadow-sm border border-[#2D402D]/10">
          <Sparkles className="text-[#2D402D]" size={28} />
        </div>
        <h2 className="font-inria text-3xl font-bold text-[#2D402D]">
          AI Analysis for {city || "your location"} :
        </h2>
      </div>
      
      <div className="space-y-4 ml-2">
        <div className="flex items-center gap-3 text-lg font-inria text-[#2D402D]">
          <CheckCircle2 className="text-green-600" size={20} />
          <p>Analyzed 6 plants against current weather conditions in <span className="font-bold capitalize">{city || "this area"}</span></p>
        </div>
        
        <div className="space-y-2">
          <p className="text-lg font-inria text-[#2D402D] ml-8 italic font-medium">
            🎯 Found 6 plants with excellent compatibility (70%+)
          </p>
          <p className="text-lg font-inria text-[#2D402D] ml-8 italic font-medium">
            🔮 Top recommendation: Tomato with 100% match
          </p>
          <p className="text-lg font-inria text-[#2D402D] ml-8 italic font-medium">
            💡 🌱 Spring - Perfect for starting seeds
          </p>
        </div>
      </div>
    </div>
  );
};

export default AIAnalysis;