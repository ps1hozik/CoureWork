import {
  Button,
  Table,
  Thead,
  Tbody,
  Tr,
  Th,
  Td,
  TableContainer,
  Popover,
  PopoverTrigger,
  PopoverArrow,
  PopoverContent,
  PopoverCloseButton,
  PopoverBody,
} from "@chakra-ui/react";

export default function TableView({ products }) {
  return (
    <Table variant="striped" colorScheme="teal" mt={10}>
      <Thead>
        <Tr>
          <Th>Название</Th>
          <Th>Производитель</Th>
          <Th>Штрих-код</Th>
          <Th>Цена</Th>
          <Th>Количество</Th>
          <Th>Забронировано</Th>
        </Tr>
      </Thead>
      <Tbody>
        {products.map((product, index) => (
          <Tr key={index}>
            <Td>{product.name}</Td>
            <Td>{product.manufacturer}</Td>
            <Td>{product.barcode}</Td>
            <Td>{product.price}</Td>
            <Td>{product.total_quantity}</Td>
            <Td>{product.booked_quantity}</Td>
            <Td>
              <Popover>
                <PopoverTrigger>
                  <Button
                    m={0}
                    p={0}
                    b={0}
                    size="md"
                    outline="none"
                    colorScheme="teal"
                    variant="link"
                  >
                    Описание
                  </Button>
                </PopoverTrigger>
                <PopoverContent>
                  <PopoverArrow />
                  <PopoverCloseButton />
                  <PopoverBody p={5}>{product.description}</PopoverBody>
                </PopoverContent>
              </Popover>
            </Td>
            <Td p={0}>
              <Button colorScheme="teal">Изменить</Button>
            </Td>
            <Td p={0}>
              <Button colorScheme="teal">X</Button>
            </Td>
          </Tr>
        ))}
      </Tbody>
    </Table>
  );
}
