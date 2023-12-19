import { Box, Button, Flex, VStack, Text } from "@chakra-ui/react";
import { useNavigate } from "react-router";
import Cookies from "universal-cookie";
import AdminLayout from "../admin/main_layout";
const MainLayout = ({ children }) => {
  const cookies = new Cookies();
  const navigate = useNavigate();
  const signOut = () => {
    cookies.remove("name");
    cookies.remove("user_id");
    cookies.remove("organization_id");
    cookies.remove("warehouse_id");
    cookies.remove("role");
    navigate("/login");
  };
  const main_page = () => {
    navigate("/");
  };
  const role = cookies.get("role");
  const layout = () => {
    if (role == "Администратор") {
      return <AdminLayout />;
    }
  };

  return (
    <Flex>
      <VStack
        spacing={8}
        align="flex-start"
        bg="white"
        p={6}
        position="fixed"
        left={0}
        top={0}
        h="100vh"
      >
        <Text fontSize="xl">{cookies.get("name")}</Text>
        {layout()}
        <Button
          fontSize="md"
          onClick={signOut}
          w={150}
          position="fixed"
          bottom={4}
        >
          Выйти
        </Button>
      </VStack>

      <Box ml={200} w="100%">
        {children}
      </Box>
    </Flex>
  );
};

export default MainLayout;
