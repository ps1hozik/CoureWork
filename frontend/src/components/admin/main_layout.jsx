import { Button } from "@chakra-ui/react";
import { useNavigate } from "react-router-dom";
const AdminLayout = () => {
  const navigate = useNavigate();
  return (
    <>
      <Button
        fontSize="md"
        colorScheme="teal"
        onClick={() => navigate("/")}
        w={150}
      >
        На главную
      </Button>

      <Button
        fontSize="md"
        colorScheme="teal"
        onClick={() => navigate("/admin/find_user")}
        w={150}
        style={{ whiteSpace: "normal" }}
      >
        Поиск пользователя
      </Button>
      <Button
        fontSize="md"
        colorScheme="teal"
        w={150}
        style={{ whiteSpace: "normal" }}
        onClick={() => navigate("/admin/all_users")}
      >
        Вывести всех пользователей
      </Button>
    </>
  );
};

export default AdminLayout;
