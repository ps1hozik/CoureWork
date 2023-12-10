import { Formik, Field } from "formik";
import {
  Box,
  Button,
  Flex,
  FormControl,
  FormLabel,
  Input,
  Textarea,
  VStack,
} from "@chakra-ui/react";

import { useNavigate } from "react-router";
import Cookies from "universal-cookie";

export default function OrganizationAdd() {
  const cookies = new Cookies();
  const navigate = useNavigate();
  return (
    <Flex bg="gray.100" align="center" justify="center" h="100vh">
      <Box bg="white" p={6} rounded="md" w="50vh">
        <Formik
          initialValues={{
            name: "",
            code: "",
            description: "",
          }}
          onSubmit={(values) => {
            fetch("http://localhost:8000/organization/", {
              method: "POST",
              headers: { "Content-Type": "application/json" },
              body: JSON.stringify(values, null, 2),
            })
              .then(function (response) {
                return response.json();
              })
              .then(function (data) {
                if (data.status == "success") {
                  cookies.set("organization_id", data.data.id);
                  navigate("/warehouse_add");
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
                  <FormLabel htmlFor="code">Код организации</FormLabel>
                  <Field
                    as={Input}
                    id="code"
                    name="code"
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
