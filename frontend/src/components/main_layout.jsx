import { Box, Button, Flex, VStack, Text } from "@chakra-ui/react";
import { useNavigate } from "react-router";
import Cookies from "universal-cookie";
const MainLayout = ({ children }) => {
  const cookies = new Cookies();
  const navigate = useNavigate();
  const signOut = () => {
    cookies.remove("name");
    cookies.remove("user_id");
    cookies.remove("organization_id");
    cookies.remove("warehouse_id");
    navigate("/login");
  };
  const main_page = () => {
    navigate("/");
  };
  return (
    <Flex>
      <VStack
        spacing={8}
        align="flex-start"
        bg="white"
        p={4}
        position="fixed"
        left={0}
        top={0}
        h="100vh"
      >
        <Text fontSize="xl">{cookies.get("name")}</Text>

        <Button fontSize="md" colorScheme="teal" onClick={main_page} w={100}>
          На главную
        </Button>
        <Button
          fontSize="md"
          onClick={signOut}
          w={100}
          position="fixed"
          bottom={4}
        >
          Выйти
        </Button>
      </VStack>

      <Box ml={100} w="100%">
        {children}
      </Box>
    </Flex>
  );
};

export default MainLayout;
