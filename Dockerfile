# Stage 1: Controller application
FROM controller-image:latest AS controller

# Stage 2: Executor application
FROM executor-image:latest AS final

# Copy the controller executable from the controller image
COPY --from=controller /app .

# Expose required ports for both applications
EXPOSE 3000 8080 8081

# Add the run script to launch both applications
COPY run.sh run.sh
RUN chmod +x run.sh

# Start both applications
ENTRYPOINT ["/bin/bash", "run.sh"]
