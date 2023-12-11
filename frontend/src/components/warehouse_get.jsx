/* eslint-disable react/prop-types */
import { Box, Flex, Text, Textarea, Button } from "@chakra-ui/react";
import { Link } from "react-router-dom";
import Cookies from "universal-cookie";
import React, { useState, useEffect } from "react";
import { useNavigate } from "react-router";

const Head = () => {
  const navigate = useNavigate();
  return (
    <Flex
      bg="gray.50"
      justify="space-between"
      gap={30}
      pl={10}
      pr={10}
      zIndex={1}
      width="100%"
    >
      <Button
        colorScheme="teal"
        w="100%"
        onClick={() => {
          navigate("/warehouse_add");
        }}
      >
        Добавить
      </Button>
    </Flex>
  );
};

const WarehouseBlock = ({
  w_id,
  name,
  address,
  description,
  cookies,
  product_quantity,
}) => {
  const navigate = useNavigate();
  const chose_warehouse = () => {
    cookies.set("warehouse_id", w_id);
    navigate("/product_get");
  };

  return (
    <Box
      bg="white"
      display="flex"
      flexDirection="column"
      alignItems="center"
      rounded="md"
      mr={10}
      ml={10}
      p={6}
      mb={4}
      w={340}
    >
      <Box bg="gray.100" p={4} roundedTop="md" h={150} w="100%" maxWidth={360}>
        <Text fontWeight="bold" fontSize={30}>
          {name}
        </Text>
        <Text fontSize={15}>Адрес: {address}</Text>
        <Text fontSize={15}>Количество товаров: {product_quantity}</Text>
      </Box>
      <Textarea
        bg="gray.100"
        p={4}
        rounded="none"
        roundedBottom="md"
        h={150}
        w="100%"
        maxWidth={360}
        mb={5}
        resize="none"
        readOnly={true}
        value={description}
      />
      <Box w="full">
        <Link to={"/product_get"} className="link">
          <Button colorScheme="teal" width="full" onClick={chose_warehouse}>
            Выбрать
          </Button>
        </Link>
      </Box>
    </Box>
  );
};

export default function WarehouseList() {
  const [warehouses, setWarehouses] = useState([]);
  const cookies = new Cookies();
  const o_id = cookies.get("organization_id");

  useEffect(() => {
    fetch(`http://localhost:8000/warehouse/${o_id}`, {
      method: "GET",
      headers: { "Content-Type": "application/json" },
    })
      .then(function (response) {
        return response.json();
      })
      .then(function (data) {
        if (data.status === "success") {
          setWarehouses(data.data);
        }
      })
      .catch(function (error) {
        console.log(error, "error");
      });
  }, [o_id]);

  return (
    <>
      <Head />
      <Flex
        bg="gray.100"
        align="center"
        justify="center"
        flexWrap="wrap"
        overflow="auto"
        p={6}
      >
        {warehouses.map((warehouse) => (
          <WarehouseBlock
            key={warehouse.id}
            w_id={warehouse.id}
            name={warehouse.name}
            address={warehouse.address}
            description={warehouse.description}
            product_quantity={warehouse.product_quantity}
            cookies={cookies}
          />
        ))}
      </Flex>
    </>
  );
}
