import { useLocation, Navigate } from "react-router-dom";

export const setToken = (token) => {
  localStorage.setItem("access_token", token);
};

export const setName = (name) => {
  localStorage.setItem("name", name);
};

export const fetchToken = (token) => {
  return localStorage.getItem("access_token");
};

export function RequireToken({ children }) {
  let auth = fetchToken();
  let location = useLocation();
  console.log(auth);
  if (!auth) {
    return <Navigate to="/" state={{ from: location }} />;
  }

  return children;
}
