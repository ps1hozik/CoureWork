import { useNavigate } from "react-router-dom";
import { Box, Button, Flex } from "@chakra-ui/react";

export default function OrganizationAdd() {
  const navigate = useNavigate();
  return (
    <Flex
      bg="gray.100"
      align="center"
      justify="center"
      flexDirection="column"
      h="100vh"
    >
      <Box
        bg="white"
        align="center"
        justify="center"
        p={6}
        rounded="md"
        w="80vh"
      >
        <Button
          colorScheme="teal"
          m={4}
          onClick={() => navigate("organization_add", { replace: false })}
        >
          Добавить организацию
        </Button>
        <Button
          colorScheme="teal"
          m={4}
          onClick={() => navigate("organization_update", { replace: false })}
        >
          Изменить организацию
        </Button>
      </Box>
      <Box
        bg="white"
        align="center"
        justify="center"
        p={6}
        rounded="md"
        w="80vh"
      >
        <Button
          colorScheme="teal"
          m={4}
          onClick={() => navigate("warehouse_add", { replace: false })}
        >
          Добавить склад
        </Button>
        <Button
          colorScheme="teal"
          m={4}
          onClick={() => navigate("warehouse_update", { replace: false })}
        >
          Изменить склад
        </Button>
        <Button
          colorScheme="teal"
          m={4}
          onClick={() => navigate("warehouse_get", { replace: false })}
        >
          Посмотреть склады
        </Button>
      </Box>
    </Flex>
  );
}
