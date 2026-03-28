import { Thermometer, Droplets, Sun } from "lucide-react";

interface PlantCardProps {
  name: string;
  image: string;
  temperature: string;
  water: string;
  sunlight: string;
}

const PlantCard = ({
  name,
  image,
  temperature,
  water,
  sunlight,
}: PlantCardProps) => {
  return (
    <div className="bg-white p-6 rounded-[35px] shadow-[0_20px_50px_rgba(0,0,0,0.15)] flex flex-col items-center text-center transition-transform hover:-translate-y-2">
      {/* Plant Image */}
      <div className="w-full h-44 flex items-center justify-center mb-4">
        <img
          src={image}
          alt={name}
          className="max-w-full max-h-full object-contain"
        />
      </div>

      {/* Name */}
      <h3 className="font-inria text-3xl font-bold text-[#2D402D] mb-6 lowercase first-letter:uppercase">
        {name}
      </h3>

      {/* Stats */}
      <div className="w-full space-y-4 px-2">
        <div className="flex items-center gap-3">
          <Thermometer className="text-red-500" size={22} />
          <span className="font-inria text-lg text-[#2D402D] font-medium">
            {temperature}
          </span>
        </div>

        <div className="flex items-center gap-3">
          <Droplets className="text-blue-400 fill-blue-400" size={22} />
          <span className="font-inria text-lg text-[#2D402D] font-medium">
            {water}
          </span>
        </div>

        <div className="flex items-center gap-3">
          <Sun className="text-yellow-400 fill-yellow-400" size={22} />
          <span className="font-inria text-lg text-[#2D402D] font-medium">
            {sunlight}
          </span>
        </div>
      </div>
    </div>
  );
};

export default PlantCard;
