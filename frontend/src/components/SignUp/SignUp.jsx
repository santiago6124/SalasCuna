import React, { useContext, useState, useEffect } from "react";
import { Button, Container, Form } from "react-bootstrap";
import AuthContext from "../../context/AuthContext";
import axios from "axios"; // Import Axios for API calls


import "./SignUp.css";

const SignUp = () => {
  const [role, setRole] = useState("");
  const [rolesList, setRolesList] = useState([]); // State to store the list of roles

  const { signupUser } = useContext(AuthContext);

  const handleRoleChange = (event) => {
    setRole(event.target.value);
  };

  useEffect(() => {
    // Fetch the roles from the backend API
    const fetchRoles = async () => {
      try {
        const response = await axios.get("http://127.0.0.1:8000/api/RoleViewSet/?exclude_directora");
        setRolesList(response.data); // Update the state with the list of roles
      } catch (error) {
        console.error("Error fetching roles:", error);
      }
    };

    fetchRoles();
  }, []);

  return (
    <div className="body">
      <div className=".contenedor-form-wrapper">
        <Container fluid className="conteiner-form-signup">
          <Form onSubmit={signupUser}>
            <h1 className="titulo">Crear Usuario</h1>
            <div className="contenedor-linea">
              <hr className="linea"></hr>
            </div>

            <div className="Form-Control">
              {/* Email Label */}
              <Form.Group className="mb-3">
                <Form.Label className="mb-1">E-mail</Form.Label>
                <Form.Control
                  type="text"
                  placeholder="Ingresar E-mail"
                  name="email"
                  required
                />
              </Form.Group>
            </div>
            <div className="form-row">
              {/* Nombre Label */}
              <div className="col-md-6 mb-3">
                <Form.Label className="mb-1">Nombre</Form.Label>
                <Form.Control
                  type="text"
                  placeholder="Ingresar nombre"
                  name="first_name"
                  required
                />
              </div>

              {/* Apellido Label */}
              <div className="col-md-6 mb-3">
                <Form.Label className="mb-1">Apellido</Form.Label>
                <Form.Control
                  type="text"
                  placeholder="Ingresar Apellido"
                  name="last_name"
                  required
                />
              </div>
            </div>
            <div className="form-row">
              {/* DNI  Label*/}
              <div className="col-md-6 mb-3">
                <Form.Label className="mb-1">DNI</Form.Label>
                <Form.Control
                  type="int"
                  placeholder="Ingresar El Dni"
                  name="dni"
                  required
                />
              </div>

              {/* Rol label (Dropdown) */}
              <div className="col-md-6 mb-3">
                <Form.Label className="mb-1">Rol</Form.Label>
                <Form.Select
                  as="select"
                  name="role"
                  value={role}
                  onChange={handleRoleChange}
                  required
                >
                  <option value="" disabled selected>
                    Seleccionar Rol
                  </option>
                  {rolesList.map((role) => (
                    <option key={role.id} value={role.id}>
                      {role.name}
                    </option>
                  ))}
                </Form.Select>
              </div>
            </div>

            {/*Phone number Label*/}
            <div className="Form-Control">
              <Form.Group className="mb-3">
                <Form.Label className="mb-1 ">Numero De Telefono</Form.Label>
                <Form.Control
                  className="form-label"
                  type="number"
                  placeholder="Ingresar Nro De Telefono"
                  name="phone_number"
                  required
                />
              </Form.Group>
            </div>

            <div className="form-row">
              {/* Ciudad */}
              <div className="col-md-6 mb-3">
                <Form.Label className="mb-1">Ciudad</Form.Label>
                <Form.Control
                  type="text"
                  placeholder="Ingresar Ciudad"
                  name="city"
                  required
                />
              </div>

              {/* Departamento */}
              <div className="col-md-6 mb-3">
                <Form.Label className="mb-1">Departamento</Form.Label>
                <Form.Control
                  type="text"
                  placeholder="Ingresar Departamento"
                  name="department"
                  required
                />
              </div>
            </div>
            <div className="Form-Control">
              {/*Address Label*/}
              <Form.Group className="mb-3">
                <Form.Label className="mb-1">Direccion</Form.Label>
                <Form.Control
                  type="text"
                  placeholder="Ingresar Direccion"
                  name="address"
                  required
                />
              </Form.Group>
            </div>
            <div className="Form-Control">
              {/*Password Label*/}
              <Form.Group className="mb-3">
                <Form.Label className="mb-1">Contraseña</Form.Label>
                <Form.Control
                  type="password"
                  placeholder="Ingrese su contraseña"
                  name="password"
                  minLength="8"
                  required
                />
              </Form.Group>
            </div>

            <div className="Form-Control">
              {/*Repeat Password Label*/}
              <Form.Group className="mb-3">
                <Form.Label className="mb-1">Repetir Contraseña</Form.Label>
                <Form.Control
                  type="password"
                  placeholder="Ingrese su contraseña de nuevo"
                  name="re_password"
                  minLength="8"
                  required
                />
              </Form.Group>
            </div>

            <div className="contenedor-boton-createuser">
              <Button
                className="boton mt-3"
                boton
                variant="primary"
                type="submit"
              >
                Ingresar
              </Button>
            </div>
          </Form>
        </Container>
      </div>
    </div>
  );
};

export default SignUp;
