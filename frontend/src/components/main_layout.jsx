import { Box, Button, Flex, VStack, Text } from "@chakra-ui/react";
import { useNavigate } from "react-router";
import Cookies from "universal-cookie";
const MainLayout = ({ children }) => {
  const cookies = new Cookies();
  const navigate = useNavigate();
  const signOut = () => {
    cookies.remove("name");
    navigate("/login");
  };
  const main_page = () => {
    navigate("/");
  };
  return (
    <Box>
      <Flex justify-content="space-between">
        <VStack spacing={8} align="flex-start" bg="white" p={4}>
          <Text fontSize="xl">{cookies.get("name")}</Text>

          <Button fontSize="md" colorScheme="teal" onClick={main_page} w={100}>
            На главную
          </Button>
          <Button fontSize="md" onClick={signOut} w={100}>
            Выйти
          </Button>
        </VStack>

        <Box w="100%" h="100%">
          {children}
        </Box>
      </Flex>

      <Box position="fixed" bottom={4} left={4}></Box>
    </Box>
  );
};

export default MainLayout;
