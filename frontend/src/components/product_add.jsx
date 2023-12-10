/* eslint-disable react/prop-types */
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
import Cookies from "universal-cookie";
import { useNavigate } from "react-router";

export default function ProductAdd({ text }) {
  const navigate = useNavigate();
  const cookies = new Cookies();
  return (
    <Flex bg="gray.100" align="center" justify="center" p={10}>
      <Box bg="white" p={6} rounded="md" w={400}>
        <Formik
          initialValues={{
            name: "",
            manufacturer: "",
            barcode: "",
            price: "",
            total_quantity: "",
            booked_quantity: "",
            descriptin: "",
          }}
          onSubmit={(values) => {
            const w_id = cookies.get("warehouse_id");

            fetch(`http://localhost:8000/product/${w_id}`, {
              method: "POST",
              headers: { "Content-Type": "application/json" },
              body: JSON.stringify(values, null, 2),
            })
              .then(function (response) {
                return response.json();
              })
              .then(function (data) {
                if (data.status == "success") {
                  navigate("/product_get");
                }
              })
              .catch(function (error) {
                console.log(error, "error");
              });
          }}
        >
          {({ handleSubmit }) => (
            <form onSubmit={handleSubmit}>
              <VStack spacing={4}>
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
                  <FormLabel htmlFor="manufacturer">Производитель</FormLabel>
                  <Field
                    as={Input}
                    id="manufacturer"
                    name="manufacturer"
                    type="text"
                    variant="filled"
                  />
                </FormControl>

                <FormControl>
                  <FormLabel htmlFor="price">Цена</FormLabel>
                  <Field
                    as={Input}
                    id="price"
                    name="price"
                    type="number"
                    variant="filled"
                  />
                </FormControl>

                <FormControl>
                  <FormLabel htmlFor="barcode">Штрих-код</FormLabel>
                  <Field
                    as={Input}
                    id="barcode"
                    name="barcode"
                    type="number"
                    variant="filled"
                  />
                </FormControl>
                <FormControl>
                  <FormLabel htmlFor="total_quantity">Количество</FormLabel>
                  <Field
                    as={Input}
                    id="total_quantity"
                    name="total_quantity"
                    type="number"
                    variant="filled"
                  />
                </FormControl>
                <FormControl>
                  <FormLabel htmlFor="booked_quantity">Забронировано</FormLabel>
                  <Field
                    as={Input}
                    id="booked_quantity"
                    name="booked_quantity"
                    type="number"
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
                  {text}
                </Button>
              </VStack>
            </form>
          )}
        </Formik>
      </Box>
    </Flex>
  );
}
