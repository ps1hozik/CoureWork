import { Link } from "react-router-dom";
import { Box, Button, Flex, VStack, Text } from "@chakra-ui/react";
import { useNavigate } from "react-router";

const MainLayout = ({ children }) => {
  console.log(localStorage.getItem("name"));
  const navigate = useNavigate();
  const signOut = () => {
    localStorage.removeItem("access_token");
    localStorage.removeItem("name");
    navigate("/login");
  };
  const main_page = () => {
    navigate("/");
  };
  return (
    <Box>
      <Flex justify-content="space-between">
        <VStack spacing={8} align="flex-start" bg="white" p={4}>
          <Text fontSize="xl">{localStorage.getItem("name")}</Text>

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
