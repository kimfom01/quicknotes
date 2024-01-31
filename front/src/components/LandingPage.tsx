import { Button, Stack, Image } from "react-bootstrap";
import { Base } from "./Base";
import student from "../assets/landing-woman.png";
import scribble1 from "../assets/scribble1.png";
import scribble2 from "../assets/scribble2.png";
import landing_text from "../assets/landing-text.png";
import "./LandingPage.css";

export const LandingPage = () => {
  return (
    <Base>
      <Stack className="flex-sm-column flex-lg-row" gap={3}>
        <Stack className="hero-text" gap={4}>
          <Image className="w-75" src={landing_text} alt="Landing text" />
          <Stack direction="horizontal" gap={3}>
            <Button
              as="a"
              href="/signin"
              style={{ background: "#ceff8d", color: "#1889ac" }}
              size="lg"
            >
              Get Started
            </Button>
            <Button
              as="a"
              href="how-it-works"
              size="lg"
              variant="outline-light"
            >
              Learn More
            </Button>
          </Stack>
        </Stack>
        <span>
          <Image
            className="scribble1 d-none d-lg-block"
            src={scribble1}
            alt="scribble 1"
          />
        </span>
        <div className="dotted-circle">
          <div className="middle-circle w-100 h-100">
            <div className="inner-circle w-100 h-100">
              <Image
                className="student"
                src={student}
                alt="student holding books"
              />
            </div>
          </div>
        </div>
        <span>
          <Image
            className="scribble2 d-none d-lg-block"
            src={scribble2}
            alt="scribble 2"
          />
        </span>
      </Stack>
    </Base>
  );
};
