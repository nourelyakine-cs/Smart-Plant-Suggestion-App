import PlantCard from "./PlantCard";
import { Target, Loader2 } from "lucide-react";
import type { PlantData } from "@/pages/Index";

interface CategoriesProps {
  plants: PlantData[];
}

const WATER_LABELS: Record<string, string> = {
  "faible": "Low water needs",
  "moyen": "Moderate water needs",
  "élevé": "High water needs",
  "très faible": "Very low water needs",
};

const SUN_LABELS: Record<string, string> = {
  "plein soleil": "Full sun",
  "mi-ombre": "Partial shade",
  "ombre": "Shade",
};

const Categories = ({ plants }: CategoriesProps) => {
  if (!plants || plants.length === 0) {
    return (
      <section className="bg-background py-8 px-6">
        <div className="max-w-7xl mx-auto text-center py-12">
          <Loader2 size={40} className="animate-spin text-[#2D402D] mx-auto mb-4" />
          <p className="font-inria text-[#2D402D] text-lg">Loading plant suggestions...</p>
        </div>
      </section>
    );
  }

  return (
    <section className="bg-background py-8 px-6">
      <div className="max-w-7xl mx-auto">
        <div className="flex items-center gap-3 mb-10">
          <Target size={30} className="text-[#8B9D44]" />
          <h2 className="font-inria text-4xl font-bold text-[#2D402D]">
            Best plants for you:
          </h2>
        </div>

        <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-10">
          {plants.map((plant) => (
            <PlantCard
              key={plant.key}
              name={plant.name}
              category={plant.category}
              temperature={`${plant.temp_optimal[0]}–${plant.temp_optimal[1]}°C optimal`}
              water={WATER_LABELS[plant.water_needs] || plant.water_needs}
              sunlight={SUN_LABELS[plant.sun_needs] || plant.sun_needs}
              matchScore={plant.match_score}
              difficulty={plant.difficulty}
            />
          ))}
        </div>
      </div>
    </section>
  );
};

export default Categories;
