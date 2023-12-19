import { Box, Button, Flex, Input, Text } from "@chakra-ui/react";
import Cookies from "universal-cookie";

import { useNavigate } from "react-router";
import { useState } from "react";

export default function Login() {
  const cookies = new Cookies();
  const navigate = useNavigate();
  const [id, setId] = useState(0);
  const [user, setUser] = useState([]);
  const current_id = cookies.get("user_id");
  const findUser = () => {
    console.log(typeof id);
    fetch(`http://localhost:8000/admin/${id}?current_id=${current_id}`, {
      method: "GET",
      headers: { "Content-Type": "application/json" },
    })
      .then(function (response) {
        return response.json();
      })
      .then(function (response) {
        if (response.status === "success") {
          setUser(response.data);
        } else if (response.detail.status === "error") {
          alert(JSON.stringify(response.detail, null, 2));
          console.log(JSON.stringify(response.detail, null, 2));
        }
      })
      .catch(function (error) {
        alert(error);
        console.log(error);
      });
  };

  return (
    <Flex bg="gray.100" align="top" justify="center" h="100vh">
      <Box bg="white" p={3} rounded="md">
        Введите id пользователя:
        <Input
          placeholder="id"
          colorScheme="teal"
          type="number"
          mt={5}
          onChange={(e) => setId(parseInt(e.target.value))}
        />
        <Button colorScheme="teal" mt={5} w="100%" onClick={findUser}>
          Найти
        </Button>
        <Text fontSize="3xl">
          id: <b>{user.id}</b>
        </Text>
        <Text fontSize="3xl">
          name: <b>{user.name}</b>
        </Text>
        <Text fontSize="3xl">
          login: <b>{user.login}</b>
        </Text>
        <Text fontSize="3xl">
          post: <b>{user.post}</b>
        </Text>
        <Text fontSize="3xl">
          organization_id: <b>{user.organization_id}</b>
        </Text>
        <Text fontSize="3xl">
          warehouse_id: <b>{user.warehouse_id}</b>
        </Text>
        <Text fontSize="3xl">
          role: <b>{user.role_name}</b>
        </Text>
      </Box>
    </Flex>
  );
}
