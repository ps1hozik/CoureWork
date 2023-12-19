import AdminAllUsers from "./components/admin/all_users";
import AdminFindUser from "./components/admin/find_user";
import MainPage from "./components/common/main";
import MainLayout from "./components/common/main_layout";
import Login from "./components/auth/login";
import Registration from "./components/auth/registration";
import OrganizationAdd from "./components/organization/organization_add";
import WarehouseAdd from "./components/warehouse/warehouse_add";
import WarehouseGet from "./components/warehouse/warehouse_get";
import ProductAdd from "./components/product/product_add";
import ProductGet from "./components/product/product_get";
import ProductUpdate from "./components/product/update_product";
import Unauthorized from "./components/common/unauthorized";
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
      path: "/admin/all_users",

      element: isAuthenticated ? (
        <MainLayout>
          <AdminAllUsers />
        </MainLayout>
      ) : (
        <Unauthorized />
      ),
    },
    {
      path: "/admin/find_user",

      element: isAuthenticated ? (
        <MainLayout>
          <AdminFindUser />
        </MainLayout>
      ) : (
        <Unauthorized />
      ),
    },
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
}

export default App;
