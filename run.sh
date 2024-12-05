# Start the executor application in the background
./src/ExecutorApp &

# Start the controller application in the background
sleep 10 
./app &

# Wait for both processes to complete
wait
