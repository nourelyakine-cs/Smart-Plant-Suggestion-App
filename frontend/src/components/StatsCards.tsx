import { Trophy, Calendar, Droplets } from "lucide-react";

const StatsCards = () => {
  const stats = [
    {
      title: "Top Recommendation",
      value: "Tomato",
      desc: "100% match with your climate.",
      icon: <Trophy className="text-[#8B9D44]" size={32} />,
      bgColor: "bg-[#F9FFF9]",
    },
    {
      title: "Best Season",
      value: "Spring",
      desc: "Perfect for starting seeds!",
      icon: <Calendar className="text-[#8B9D44]" size={32} />,
      bgColor: "bg-white",
    },
    {
      title: "Watering Tip",
      value: "Daily",
      desc: "Keep the soil moist but not wet.",
      icon: <Droplets className="text-[#8B9D44]" size={32} />,
      bgColor: "bg-[#F9FFF9]",
    },
  ];

  return (
    <div className="grid grid-cols-1 md:grid-cols-3 gap-6 my-8">
      {stats.map((item, index) => (
        <div
          key={index}
          className={`${item.bgColor} border border-[#2D402D]/10 p-8 rounded-[32px] shadow-sm flex flex-col items-center text-center transition-transform hover:scale-105 duration-300`}
        >
          <div className="mb-4 p-3 bg-white rounded-2xl shadow-sm border border-[#2D402D]/5">
            {item.icon}
          </div>

          <h3 className="font-inria italic text-[#2D402D]/60 text-lg mb-1">
            {item.title}
          </h3>

          <h2 className="font-inria font-bold text-[#2D402D] text-3xl mb-2">
            {item.value}
          </h2>

          <p className="font-inria text-[#556B55] text-sm leading-relaxed">
            {item.desc}
          </p>
        </div>
      ))}
    </div>
  );
};

export default StatsCards;
