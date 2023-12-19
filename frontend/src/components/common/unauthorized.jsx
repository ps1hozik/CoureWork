import { Button, Box, Text } from "@chakra-ui/react";
import { useNavigate } from "react-router";

const Unauthorized = () => {
  const navigate = useNavigate();

  return (
    <Box align="center" justifyContent="center" p="20">
      <Text fontSize="6xl">Вы не авторизованны</Text>

      <Button
        fontSize="3xl"
        colorScheme="teal"
        onClick={() => navigate("/login")}
        w="50%"
      >
        Войти
      </Button>
    </Box>
  );
};

export default Unauthorized;
