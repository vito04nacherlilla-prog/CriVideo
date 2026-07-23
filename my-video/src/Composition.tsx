import { Composition } from "remotion";
import { FocacciaVideo } from "./FocacciaVideo";
import { FPS, HEIGHT, totalDurationInFrames, WIDTH } from "./lib/scenes";

export const MyComposition = () => {
  return (
    <Composition
      id="FocacciaBarese"
      component={FocacciaVideo}
      durationInFrames={totalDurationInFrames()}
      fps={FPS}
      width={WIDTH}
      height={HEIGHT}
    />
  );
};
