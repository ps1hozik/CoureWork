import { Formik, Field } from "formik";
import {
  Box,
  Button,
  Flex,
  FormControl,
  FormLabel,
  FormErrorMessage,
  Input,
  VStack,
  Text,
} from "@chakra-ui/react";

import { fetchToken, setToken, setName } from "./auth";
import { useNavigate } from "react-router";

export default function Login() {
  const navigate = useNavigate();
  const register = () => {
    navigate("/registration");
  };
  return (
    <Flex bg="gray.100" align="center" justify="center" h="100vh">
      <Box bg="white" p={6} rounded="md" w="50vh">
        <Formik
          initialValues={{
            login: "",
            password: "",
          }}
          onSubmit={(values) => {
            fetch("http://localhost:8000/user/login", {
              method: "POST",
              headers: { "Content-Type": "application/json" },
              body: JSON.stringify(values, null, 2),
            })
              .then(function (response) {
                return response.json();
              })
              .then(function (data) {
                console.log(data.access_token, "response.data.access_token\n");
                console.log(data.name, "response.data.name\n");
                console.log(data, "response.data\n");

                if (data.access_token) {
                  setToken(data.access_token);
                  setName(data.name);
                  navigate("/warehouse_add");
                }
              })
              .catch(function (error) {
                console.log(error, "error");
              });
          }}
        >
          {({ handleSubmit, errors, touched }) => (
            <form onSubmit={handleSubmit}>
              <VStack spacing={4} align="flex-start">
                <FormControl>
                  <FormLabel htmlFor="login">Логин</FormLabel>
                  <Field
                    as={Input}
                    id="login"
                    name="login"
                    type="text"
                    variant="filled"
                  />
                </FormControl>
                <FormControl isInvalid={!!errors.password && touched.password}>
                  <FormLabel htmlFor="password">Пароль</FormLabel>
                  <Field
                    as={Input}
                    id="password"
                    name="password"
                    type="password"
                    variant="filled"
                    validate={(value) => {
                      let error;

                      if (value.length < 6) {
                        error = "Password must contain at least 6 characters";
                      }

                      return error;
                    }}
                  />
                  <FormErrorMessage>{errors.password}</FormErrorMessage>
                </FormControl>
                <Button type="submit" colorScheme="teal" width="full">
                  Войти
                </Button>

                <Button
                  mt={4}
                  size="sm"
                  colorScheme="teal"
                  width="full"
                  onClick={register}
                >
                  Зарегестрироваться
                </Button>
              </VStack>
            </form>
          )}
        </Formik>
      </Box>
    </Flex>
  );
}
