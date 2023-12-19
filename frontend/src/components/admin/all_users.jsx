import { Button, Table, Thead, Tbody, Tr, Th, Td } from "@chakra-ui/react";

import { useState, useEffect, useRef } from "react";
import Cookies from "universal-cookie";

export default function TableView({ products }) {
  const cookies = new Cookies();
  const current_id = cookies.get("user_id");

  const [users, setUsers] = useState([]);
  const [roles, setRoles] = useState([]);
  const [showPrompt, setShowPrompt] = useState(false);
  const [userId, setUserId] = useState(0);
  const fetchData = () => {
    fetch(`http://localhost:8000/admin/?current_id=${current_id}`, {
      method: "GET",
      headers: { "Content-Type": "application/json" },
    })
      .then(function (response) {
        return response.json();
      })
      .then(function (response) {
        if (response.status === "success") {
          setUsers(response.data.users);
          setRoles(response.data.roles);
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

  useEffect(() => {
    fetchData();
  }, []);
  const addRole = (userId) => {
    setShowPrompt(true);
    setUserId(userId);
  };

  useEffect(() => {
    if (showPrompt) {
      const roleNum = prompt(
        `Пожалуйста, введите номер роли:\n${JSON.stringify(roles, null)}`
      );
      if (roleNum) {
        const currentId = cookies.get("user_id");
        const url = `http://localhost:8000/admin/role/${userId}?current_id=${currentId}&role_num=${roleNum}`;

        fetch(url, {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
        })
          .then(function (response) {
            return response.json();
          })
          .then(function (response) {
            if (response.status === "success") {
              fetchData();
              console.log(response.details);
            } else if (response.detail.status === "error") {
              alert(JSON.stringify(response.detail, null, 2));
              console.log(JSON.stringify(response.detail, null, 2));
            }
          })
          .catch(function (error) {
            console.log(error);
          });
      }
      setShowPrompt(false);
    }
  }, [showPrompt, userId]);

  const removeRole = (userId) => {
    const currentId = cookies.get("user_id");
    const url = `http://localhost:8000/admin/role/${userId}?current_id=${currentId}`;

    fetch(url, {
      method: "DELETE",
      headers: {
        "Content-Type": "application/json",
      },
    })
      .then(function (response) {
        return response.json();
      })
      .then(function (response) {
        if (response.status === "success") {
          fetchData();
          console.log(response.details);
        } else if (response.detail.status === "error") {
          alert(JSON.stringify(response.detail, null, 2));
          console.log(JSON.stringify(response.detail, null, 2));
        }
      })
      .catch(function (error) {
        console.log(error);
      });
  };

  return (
    <Table variant="striped" colorScheme="teal" mt={10}>
      <Thead>
        <Tr>
          <Th>id</Th>
          <Th>name</Th>
          <Th>login</Th>
          <Th>post</Th>
          <Th textAlign="center">organization_id</Th>
          <Th textAlign="center">warehouse_id</Th>
          <Th>role_name</Th>
        </Tr>
      </Thead>
      <Tbody>
        {users.map((user, index) => (
          <Tr key={index}>
            <Td>{user.id}</Td>
            <Td>{user.name}</Td>
            <Td>{user.login}</Td>
            <Td>{user.post}</Td>
            <Td textAlign="center">{user.organization_id}</Td>
            <Td textAlign="center">{user.warehouse_id}</Td>
            <Td>{user.role_name}</Td>
            <Td p={0}>
              <Button colorScheme="teal" onClick={() => addRole(user.id)}>
                Добавить роль
              </Button>
            </Td>
            <Td p={0}>
              <Button colorScheme="teal" onClick={() => removeRole(user.id)}>
                Удалить роль
              </Button>
            </Td>
          </Tr>
        ))}
      </Tbody>
    </Table>
  );
}
