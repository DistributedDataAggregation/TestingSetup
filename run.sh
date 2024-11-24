ls -la
ls -la src

# Start the executor application in the background
./src/ExecutorApp &

sleep 5 

# Start the controller application in the background
./app &

# Wait for both processes to complete
wait
