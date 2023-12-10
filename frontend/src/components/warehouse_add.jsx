import { Formik, Field } from "formik";
import {
  Box,
  Button,
  Flex,
  FormControl,
  FormLabel,
  Textarea,
  Input,
  VStack,
} from "@chakra-ui/react";

import { useNavigate } from "react-router";
import Cookies from "universal-cookie";

export default function WarehouseAdd() {
  const cookies = new Cookies();
  const navigate = useNavigate();
  return (
    <Flex bg="gray.100" align="center" justify="center" h="100vh">
      <Box bg="white" p={6} rounded="md" w="50vh">
        <Formik
          initialValues={{
            name: "",
            address: "",
            description: "",
          }}
          onSubmit={(values) => {
            const o_id = cookies.get("organization_id");

            fetch(`http://localhost:8000/warehouse/${o_id}`, {
              method: "POST",
              headers: { "Content-Type": "application/json" },
              body: JSON.stringify(values, null, 2),
            })
              .then(function (response) {
                return response.json();
              })
              .then(function (data) {
                if (data.status == "success") {
                  navigate("/warehouse_get");
                }
              })
              .catch(function (error) {
                console.log(error, "error");
              });
          }}
        >
          {({ handleSubmit }) => (
            <form onSubmit={handleSubmit}>
              <VStack spacing={4} align="flex-start">
                <FormControl>
                  <FormLabel htmlFor="name">Название</FormLabel>
                  <Field
                    as={Input}
                    id="name"
                    name="name"
                    type="text"
                    variant="filled"
                  />
                </FormControl>
                <FormControl>
                  <FormLabel htmlFor="address">Адрес</FormLabel>
                  <Field
                    as={Input}
                    id="address"
                    name="address"
                    type="text"
                    variant="filled"
                  />
                </FormControl>

                <FormControl paddingTop={10}>
                  <FormLabel htmlFor="description">Описание</FormLabel>
                  <Field
                    as={Textarea}
                    id="description"
                    name="description"
                    variant="filled"
                    resize="none"
                  />
                </FormControl>

                <Button type="submit" colorScheme="teal" width="full">
                  Создать
                </Button>
              </VStack>
            </form>
          )}
        </Formik>
      </Box>
    </Flex>
  );
}
