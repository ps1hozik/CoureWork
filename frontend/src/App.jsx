import MainPage from "./components/main";
import MainLayout from "./components/main_layout";
import Login from "./components/login";
import Registration from "./components/registration";
import OrganizationAdd from "./components/organization_add";
import WarehouseAdd from "./components/warehouse_add";
import WarehouseGet from "./components/warehouse_get";
import ProductAdd from "./components/product_add";
import ProductGet from "./components/product/product_get";
import { Route, Routes } from "react-router";
import { RequireToken } from "./components/auth";

function App() {
  return (
    <Routes>
      <Route path="/" element={<MainLayout children={<MainPage />} />} />
      <Route path="login" element={<Login />} />
      <Route path="registration" element={<Registration />} />
      <Route
        path="organization_add"
        element={
          <RequireToken>
            <OrganizationAdd />
          </RequireToken>
        }
      />
      <Route
        path="warehouse_add"
        element={
          <MainLayout
            children={
              <RequireToken>
                <WarehouseAdd />
              </RequireToken>
            }
          />
        }
      />
      <Route
        path="warehouse_get"
        element={<MainLayout children={<WarehouseGet />} />}
      />
      <Route
        path="product_add"
        element={<MainLayout children={<ProductAdd text="Добавить" />} />}
      />
      <Route
        path="product_get"
        element={<MainLayout children={<ProductGet />} />}
      />
      <Route
        path="product_update"
        element={<MainLayout children={<ProductAdd text="Изменить" />} />}
      />
    </Routes>
  );
}

export default App;
