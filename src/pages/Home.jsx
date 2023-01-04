import useStockCalls from "../hooks/useStockCalls";



const Home = () => {

  const {getFirms} = useStockCalls()

  return <div>Home</div>;
};

export default Home;
