import PlantCard from "./PlantCard";
import tomatoImg from "@/assets/tomato.png";
import sunflowerImg from "@/assets/sunflower.png";
import parsleyImg from "@/assets/parsley.png";
import cucumberImg from "@/assets/cucumber.png";
import onionImg from "@/assets/onion.png";
import strawberryImg from "@/assets/strawberry.png";
import { Target } from "lucide-react";

const plants = [
  {
    name: "Tomato",
    image: tomatoImg,
    temperature: "18-25°C ideal",
    water: "High",
    sunlight: "Full",
  },
  {
    name: "Sunflower",
    image: sunflowerImg,
    temperature: "64°F - 90°F",
    water: "Moderate",
    sunlight: "Full",
  },
  {
    name: "Parsley",
    image: parsleyImg,
    temperature: "18-25°C ideal",
    water: "High",
    sunlight: "Full",
  },
  {
    name: "Cucumber",
    image: cucumberImg,
    temperature: "18-25°C ideal",
    water: "High",
    sunlight: "Full",
  },
  {
    name: "Onion",
    image: onionImg,
    temperature: "18-25°C ideal",
    water: "High",
    sunlight: "Full",
  },
  {
    name: "Strawberry",
    image: strawberryImg,
    temperature: "18-25°C ideal",
    water: "High",
    sunlight: "Full",
  },
];

const Categories = () => {
  return (
    <section className="bg-background py-8 px-6">
      <div className="max-w-7xl mx-auto">
        <div className="flex items-center gap-3 mb-10">
          <Target size={30} className="text-[#8B9D44]" />
          <h1 className="font-inria text-4xl font-bold text-[#2D402D]">
            plants :
          </h1>
        </div>

        <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-10">
          {plants.map((plant) => (
            <PlantCard key={plant.name} {...plant} />
          ))}
        </div>
      </div>
    </section>
  );
};

export default Categories;
