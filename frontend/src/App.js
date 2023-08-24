import React from "react";
import { BrowserRouter as Router, Route, Routes } from "react-router-dom";
import { AuthProvider } from "./context/AuthContext";
import "./App.css";
import Navbar from "./components/Menu/Menu";
import PrivateRoute from "./utils/PrivateRoute";
import { PublicRoute } from "./utils/PublicRoute";

import Activate from "./containers/Activate";
import Home from "./containers/Home";
import ResetPassword from "./containers/ResetPassword";
import ResetPasswordConfirm from "./containers/ResetPasswordConfirm";
import Signup from "./components/SignUp/SignUp";
import { Login } from "./components/Login/Login";
import ActivateAccountPage from "./pages/ActivateAccountPage/ActivateAccountPage";
import GeneratePadron from "./components/GeneratePadron/GeneratePadron";
import TechnicalReport from "./components/TechnicalReport/TechnicalReport";
import AddChildrenPage from "./pages/AddChildrenPage/AddChildrenPage";
import CreateRoomPage from "./pages/CreateRoomPage/CreateRoomPage";
import { SelectRoom } from "./components/SelectRoom/SelectRoom";
import { FormAddChildren } from "./components/FormAddChildren/FormAddChildren";
import Payout from "./components/Payout/Payout";
import CribroomDashboard from "./components/CribroomDashboard/CribroomDashboard";
import { FaExpeditedssl } from "react-icons/fa";
import { FormEditChildren } from "../src/components/FormEditChildren/FormEditChildren";

function App() {
  return (
    <Router>
      <div className="App">
        <AuthProvider>
          <Routes>
            <Route exact path="/" element={<Home />} />
            <Route
              path="/login"
              element={<PublicRoute children={<Login />} />}
            />
            <Route
              path="/signup"
              element={<PublicRoute children={<Signup />} />}
            />
            <Route
              path="/reset-password"
              element={<PublicRoute children={<ResetPassword />} />}
            />
            <Route
              path="/password/reset/confirm/:uid/:token"
              element={<PublicRoute children={<ResetPasswordConfirm />} />}
            />
            <Route
              path="/activate/:uid/:token"
              element={<ActivateAccountPage />}
            />

            <Route
              path="/generate-padron"
              element={<PublicRoute children={<GeneratePadron />} />}
            />

            <Route
              path="/añadir-chico"
              element={<PublicRoute children={<AddChildrenPage />} />}
            />

            <Route
              path="/children-management"
              element={<PublicRoute children={<AddChildrenPage />} />}
            />

            <Route
              path="/children-management/new"
              element={<PublicRoute children={<FormAddChildren />} />}
            />

            <Route
              path="/children-management/edit"
              element={<PublicRoute children={<FormEditChildren />} />}
            />

            <Route
              path="/crear-sala"
              element={<PublicRoute children={<CreateRoomPage />} />}
            />
            <Route
              path="/editar-sala"
              element={<PublicRoute children={<SelectRoom />} />}
            />
            <Route
              path="/maestro-montos"
              element={<PublicRoute children={<Payout />} />}
            />
            <Route
              path="/informe-tecnico"
              element={<PublicRoute children={<TechnicalReport />} />}
            />
            <Route
              path="/gestion-sala"
              element={<PrivateRoute children={<CribroomDashboard />} />}
            />
          </Routes>
        </AuthProvider>
      </div>
    </Router>
  );
}

export default App;
