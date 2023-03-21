import React, { useState, useEffect } from "react";
import {
  createBrowserRouter,
  RouterProvider,
  useNavigate,
} from "react-router-dom";
import Dashboard from "./components/Dashboard";
import Home from "./components/home/Home";
import Signup from "./components/signin/signup";
import Login from "./components/signin/login";
import Profile from "./components/Profile";
import Loader from "./components/loader/Loader";
const Apps = () => {
  const [loading, setLoading] = useState(false);
  useEffect(() => {
    setLoading(true);
    setTimeout(() => {
      setLoading(false);
    }, 2000);
  }, []);
  const router = createBrowserRouter([
    {
      path: "/",
      element: <Loader />,
    },
    {
      path: "/home",
      element: <Home />,
    },
    {
      path: "/dashboard",
      element: <Dashboard />,
    },
    {
      path: "/signup",
      element: <Signup />,
    },
    {
      path: "/login",
      element: <Login />,
    },
    {
      path: "/profile",
      element: <Profile />,
    },
  ]);
  return <RouterProvider router={router} />;
};

export default Apps;
