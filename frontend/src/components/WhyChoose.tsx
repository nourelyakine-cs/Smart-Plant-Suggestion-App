import handPlantImg from "@/assets/hand-plant.jpg";

const WhyChoose = () => {
  return (
    <section className="container py-16">
      <h2 className="text-3xl md:text-4xl font-bold text-center mb-12 text-foreground">
        Why Choose GreenGuide ?
      </h2>

      <div className="flex flex-col md:flex-row items-center gap-10 max-w-4xl mx-auto">
        <div className="flex-1">
          <img
            src={handPlantImg}
            alt="Hand holding a seedling"
            loading="lazy"
            width={400}
            height={500}
            className="rounded-xl object-cover w-full max-w-sm shadow-lg"
          />
        </div>

        <div className="flex-1 space-y-5">
          <p className="text-base text-foreground leading-relaxed">
            <span className="font-bold">GreenGuide</span> is a smart web
            application designed to help users choose the best plants based on
            real-time weather conditions. By combining artificial intelligence
            with environmental data, our platform provides personalized plant
            recommendations, helping gardeners and farmers make better
            decisions.
          </p>
          <p className="text-base text-foreground leading-relaxed">
            Our goal is to simplify plant selection and promote sustainable and
            efficient gardening.
          </p>
          <button className="rounded-full bg-primary px-8 py-3 text-sm font-semibold text-primary-foreground transition-transform hover:scale-105">
            Explore more
          </button>
        </div>
      </div>
    </section>
  );
};

export default WhyChoose;
