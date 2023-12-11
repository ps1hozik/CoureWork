import MainPage from "./components/main";
import MainLayout from "./components/main_layout";
import Login from "./components/login";
import Registration from "./components/registration";
import OrganizationAdd from "./components/organization_add";
import WarehouseAdd from "./components/warehouse_add";
import WarehouseGet from "./components/warehouse_get";
import ProductAdd from "./components/product/product_add";
import ProductGet from "./components/product/product_get";
import ProductUpdate from "./components/product/update_product";
import Unauthorized from "./components/unauthorized";
// import { Route, Routes } from "react-router";
import { useRoutes, Navigate, Route } from "react-router-dom";
import { useEffect, useState } from "react";

import Cookies from "universal-cookie";

function App() {
  const cookie = new Cookies();

  const [isAuthenticated, setIsAuthenticated] = useState(false);
  useEffect(() => {
    const user_id = cookie.get("user_id");
    if (user_id) {
      setIsAuthenticated(true);
    } else {
      setIsAuthenticated(false);
    }
  }, []);

  useEffect(() => {
    const user_id = cookie.get("user_id");
    setIsAuthenticated(!!user_id);
  }, []);

  const routes = useRoutes([
    {
      path: "login",
      element: <Login setIsAuthenticated={setIsAuthenticated} />,
    },
    {
      path: "registration",
      element: <Registration setIsAuthenticated={setIsAuthenticated} />,
    },
    {
      path: "/",
      element: isAuthenticated ? (
        <MainLayout>
          <MainPage />
        </MainLayout>
      ) : (
        <Unauthorized />
      ),
    },
    {
      path: "/organization_add",
      element: isAuthenticated ? <OrganizationAdd /> : <Unauthorized />,
    },
    {
      path: "/warehouse_add",

      element: isAuthenticated ? (
        <MainLayout>
          <WarehouseAdd />
        </MainLayout>
      ) : (
        <Unauthorized />
      ),
    },
    {
      path: "/warehouse_get",
      element: isAuthenticated ? (
        <MainLayout>
          <WarehouseGet />
        </MainLayout>
      ) : (
        <Unauthorized />
      ),
    },
    {
      path: "/product_add",
      element: isAuthenticated ? (
        <MainLayout>
          <ProductAdd />
        </MainLayout>
      ) : (
        <Unauthorized />
      ),
    },
    {
      path: "/product_get",
      element: isAuthenticated ? (
        <MainLayout>
          <ProductGet />
        </MainLayout>
      ) : (
        <Unauthorized />
      ),
    },
    {
      path: "/product_update/:id",
      element: isAuthenticated ? (
        <MainLayout>
          <ProductUpdate />
        </MainLayout>
      ) : (
        <Unauthorized />
      ),
    },
  ]);
  return routes;
  // return (
  //   <Routes>
  //     <Route path="/" element={<MainLayout children={<MainPage />} />} />
  //     <Route path="login" element={<Login />} />
  //     <Route path="registration" element={<Registration />} />
  //     <Route path="organization_add" element={<OrganizationAdd />} />
  //     <Route
  //       path="warehouse_add"
  //       element={<MainLayout children={<WarehouseAdd />} />}
  //     />
  //     <Route
  //       path="warehouse_get"
  //       element={<MainLayout children={<WarehouseGet />} />}
  //     />
  //     <Route
  //       path="product_add"
  //       element={<MainLayout children={<ProductAdd text="Добавить" />} />}
  //     />
  //     <Route
  //       path="product_get"
  //       element={<MainLayout children={<ProductGet />} />}
  //     />
  //     <Route
  //       path="product_update/:id"
  //       element={<MainLayout children={<ProductUpdate />} />}
  //     />
  //   </Routes>
  // );
}

export default App;
