import { Link } from "react-router-dom";
import "./Error404Page.css";

export const Error404Page = () => {
  return (
    <div className="n-f-style">
      <h1>404 Page Not Found</h1>
      <h2>Oops! You seem to be lost.</h2>
      <p>
        Go to:{" "}
        <Link className="text-decoration-none" to="/">
          Home Page
        </Link>
      </p>
    </div>
  );
};
