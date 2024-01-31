import "bootstrap/dist/css/bootstrap.min.css";
import React from "react";
import ReactDOM from "react-dom/client";
import reportWebVitals from "./reportWebVitals";
import { RouterProvider, createBrowserRouter } from "react-router-dom";
import { LandingPage } from "./components/LandingPage";
import { Error404Page } from "./components/Error404Page";
import { SignIn } from "./components/SignIn";
import { SignUp } from "./components/SignUp";
import { NotesPage } from "./components/NotesPage";
import { AboutUs } from "./components/AboutUs";
import { HowItWorks } from "./components/HowItWorks";
import NavBar from "./components/NavBar";

const router = createBrowserRouter([
  {
    path: "/",
    element: <LandingPage />,
    errorElement: <Error404Page />,
  },
  {
    path: "/signin",
    element: <SignIn />,
    errorElement: <Error404Page />,
  },
  {
    path: "/signup",
    element: <SignUp />,
    errorElement: <Error404Page />,
  },
  {
    path: "/notes",
    element: <NotesPage />,
    errorElement: <Error404Page />,
  },
  {
    path: "/about-us",
    element: <AboutUs />,
    errorElement: <Error404Page />,
  },
  {
    path: "/how-it-works",
    element: <HowItWorks />,
    errorElement: <Error404Page />,
  },
  {
    path: "/nav-bar",
    element: <NavBar />,
    errorElement: <Error404Page />,
  },
  { path: "*", element: <Error404Page /> },
]);

const root = ReactDOM.createRoot(
  document.getElementById("root") as HTMLElement
);
root.render(
  <React.StrictMode>
    <RouterProvider router={router} />
  </React.StrictMode>
);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
