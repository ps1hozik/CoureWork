/* eslint-disable react/prop-types */
import { Box, Flex, Text, Textarea, Button } from "@chakra-ui/react";
import { Link } from "react-router-dom";

const WarehouseBlock = ({ index, name, address, description }) => {
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
      <Box bg="gray.100" p={4} roundedTop="md" h={120}>
        <Text fontWeight="bold" fontSize={30}>
          {name}
        </Text>
        <Text fontSize={15}>{address}</Text>
      </Box>
      <Textarea
        bg="gray.100"
        p={4}
        rounded="none"
        roundedBottom="md"
        h={150}
        mb={5}
        resize="none"
        readOnly={true}
        value={description}
      />
      <Box w="full">
        <Link to={"/product_get"} className="link">
          <Button colorScheme="teal" width="full">
            Выбрать
          </Button>
        </Link>
      </Box>
    </Box>
  );
};

export default function WarehouseList() {
  const warehouses = [
    {
      name: "Name 1",
      address: "155 Cleveland Drive South Richmond Hill, NY 11419",
      description:
        "rem Ipsum is that it has a more-or-less normal distribution of letters, as opposed to using 'Content here, content here', making it look like readable English. Many desktop publishing packages and web page editors now use Lorem Ipsum as their default model text, and",
    },

    {
      name: "Name 2",
      address: "25 Locust Lane Far Rockaway, NY 11691",
      description: "",
    },
    {
      name: "Name 3",
      address: "98 Fairground Street Lithonia, GA 30038",
      description:
        "Contrary to popular belief, Lorem Ipsum is not simply random text.",
    },
    {
      name: "Name 4",
      address: "546 Sherwood Drive Owensboro, KY 42301",
      description:
        "o be sure there isn't anything embarrassing hidden in the middle of text. All the Lorem Ipsum generators on the Internet tend to repeat predefined chunks as necessary, making this the first true generator on the Internet. It uses a dictionary of over 200 Latin words, combined with a handful of model sentence structures, to generate Lorem Ipsum which looks reasonable. The generated Lorem Ipsum is therefore always free from repetition, injected humour, or non",
    },
  ];
  return (
    <Flex
      bg="gray.100"
      align="center"
      justify="center"
      flexWrap="wrap"
      overflow="auto"
      p={6}
    >
      {warehouses.map((warehouse, index) => (
        <WarehouseBlock
          key={index}
          index={index}
          name={warehouse.name}
          address={warehouse.address}
          description={warehouse.description}
        />
      ))}
    </Flex>
  );
}
