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
import Cookies from "universal-cookie";

import { useNavigate } from "react-router";

export default function Login({ setIsAuthenticated }) {
  const cookies = new Cookies();
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
            fetch("http://localhost:8000/auth/login", {
              method: "POST",
              headers: { "Content-Type": "application/json" },
              body: JSON.stringify(values, null, 2),
            })
              .then(function (response) {
                return response.json();
              })
              .then(function (response) {
                console.log(response.data);
                if (response.status == "success") {
                  setIsAuthenticated(true);
                  cookies.set("name", response.data.name);
                  cookies.set("user_id", response.data.id);
                  cookies.set("role", response.data.role);
                  if (response.data.org_id) {
                    cookies.set("organization_id", response.data.org_id);
                    navigate("/warehouse_get");
                  } else {
                    navigate("/organization_add");
                  }
                }
                if (response.status == "error") {
                  alert(response.data);
                  console.log(response.data);
                }
              })
              .catch(function (error) {
                alert(error);
                console.log(error);
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
