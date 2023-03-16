import React from "react";
import { BrowserRouter ,Routes, Route, Link } from "react-router-dom";
import LoginForm from "./components/LoginForm";
import SignupForm from "./components/SignupForm";
import Home from "./components/Home";

const App = () => {
  return (
    <BrowserRouter>
      <div>
        <nav>
          <ul>
            <li>
              <Link to="/login">Login</Link>
            </li>
            <li>
              <Link to="/signup">Signup</Link>
            </li>
          </ul>
        </nav>

        <Routes>
          <Route path="/" component={Home} />
          <Route path="/signup" element={<SignupForm />} />
          <Route exact path="/login" element={<LoginForm />} />
        </Routes>
      </div>
    </BrowserRouter>
  );
};

export default App;
