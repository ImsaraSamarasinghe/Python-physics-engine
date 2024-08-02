import pygame
from sys import exit
from math import sqrt

class PhysicsEngine:
    def __init__(self, width=800, height=800, gravity=0.5, ball_radius=20, ball_color=(255, 0, 0)):
        pygame.init()
        self.width = width
        self.height = height
        self.gravity = gravity
        self.ball_radius = ball_radius
        self.ball_color = ball_color
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption('Physics Engine with Collisions')
        self.clock = pygame.time.Clock()
        self.balls = []
        self.click_pos = None
        self.release_pos = None

    def add_ball(self, position, velocity=(0, 0)):
        ball = {
            'pos': list(position),
            'velocity': list(velocity)
        }
        self.balls.append(ball)

    def handle_ball_collisions(self):
        for i in range(len(self.balls)):
            for j in range(i + 1, len(self.balls)):
                ball1 = self.balls[i]
                ball2 = self.balls[j]
                dx = ball1['pos'][0] - ball2['pos'][0]
                dy = ball1['pos'][1] - ball2['pos'][1]
                distance = sqrt(dx**2 + dy**2)
                
                if distance < 2 * self.ball_radius:  # Ball collision detected
                    # Calculate normal and tangent vectors
                    nx = dx / distance
                    ny = dy / distance
                    tx = -ny
                    ty = nx
                    
                    # Dot product of velocity and normal
                    dpTan1 = ball1['velocity'][0] * tx + ball1['velocity'][1] * ty
                    dpTan2 = ball2['velocity'][0] * tx + ball2['velocity'][1] * ty
                    
                    # Dot product of velocity and normal
                    dpNorm1 = ball1['velocity'][0] * nx + ball1['velocity'][1] * ny
                    dpNorm2 = ball2['velocity'][0] * nx + ball2['velocity'][1] * ny
                    
                    # Conservation of momentum in 1D
                    m1 = m2 = 1  # Assuming equal mass for simplicity
                    # Tangential velocities remain unchanged
                    vTan1 = dpTan1
                    vTan2 = dpTan2
                    # Normal velocities are exchanged
                    vNorm1 = (dpNorm1 * (m1 - m2) + 2 * m2 * dpNorm2) / (m1 + m2)
                    vNorm2 = (dpNorm2 * (m2 - m1) + 2 * m1 * dpNorm1) / (m1 + m2)
                    
                    # Update velocities to new values
                    ball1['velocity'][0] = tx * vTan1 + nx * vNorm1
                    ball1['velocity'][1] = ty * vTan1 + ny * vNorm1
                    ball2['velocity'][0] = tx * vTan2 + nx * vNorm2
                    ball2['velocity'][1] = ty * vTan2 + ny * vNorm2
                    
                    # Resolve the overlap (simple approach)
                    overlap = 2 * self.ball_radius - distance
                    ball1['pos'][0] += nx * overlap / 2
                    ball1['pos'][1] += ny * overlap / 2
                    ball2['pos'][0] -= nx * overlap / 2
                    ball2['pos'][1] -= ny * overlap / 2

    def update(self):
        # Update ball positions and velocities
        for ball in self.balls:
            # Apply gravity
            ball['velocity'][1] += self.gravity
            ball['pos'][1] += ball['velocity'][1]
            ball['pos'][0] += ball['velocity'][0]
            
            # Check for ground collision
            if ball['pos'][1] + self.ball_radius > self.height:
                ball['pos'][1] = self.height - self.ball_radius
                ball['velocity'][1] = -ball['velocity'][1] * 0.7  # Bounce with damping factor
            
            # Check for left and right wall collisions
            if ball['pos'][0] - self.ball_radius < 0:
                ball['pos'][0] = self.ball_radius
                ball['velocity'][0] = -ball['velocity'][0] * 0.7
            elif ball['pos'][0] + self.ball_radius > self.width:
                ball['pos'][0] = self.width - self.ball_radius
                ball['velocity'][0] = -ball['velocity'][0] * 0.7

        # Handle ball collisions
        self.handle_ball_collisions()

    def draw(self):
        # Clear screen
        self.screen.fill((255, 255, 255))
        
        # Draw all balls
        for ball in self.balls:
            pygame.draw.circle(self.screen, self.ball_color, (int(ball['pos'][0]), int(ball['pos'][1])), self.ball_radius)
        
        pygame.display.update()

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.click_pos = pygame.Vector2(event.pos)
                
                if event.type == pygame.MOUSEBUTTONUP:
                    self.release_pos = pygame.Vector2(event.pos)
                    if self.click_pos:
                        # Calculate velocity based on the distance and direction
                        direction = self.release_pos - self.click_pos
                        speed = direction.length() / 10  # Adjust the divisor for speed scaling
                        velocity = direction.normalize() * speed
                        self.add_ball(self.click_pos, velocity)
                        self.click_pos = None

            self.update()
            self.draw()
            self.clock.tick(60)

# Create an instance of the physics engine and run it
engine = PhysicsEngine()
engine.run()
