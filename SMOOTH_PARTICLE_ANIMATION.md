# Smooth 3D Particle Sphere - Expansion & Collapse Animation

## Overview
Enhanced 3D particle sphere with smooth expansion (ellapse) and collapse animations synchronized with speech pitch and rate in real-time.

## Key Enhancements

### 1. **Smooth Interpolation System**
- **Smoothing Factor**: 0.15 (configurable)
- **Target-based Animation**: Particles smoothly interpolate to target size
- **No Jarring Transitions**: Gradual expansion and collapse
- **Frame-by-frame Updates**: 60 FPS smooth animation

### 2. **Multi-Factor Expansion Control**

#### **Volume Expansion** (0-150px)
- Controls overall sphere size
- Higher volume = larger sphere
- Represents sound intensity

#### **Pitch Expansion** (0-80px)
- Affects expansion intensity
- Higher pitch = more expansion
- Adds vertical dimension to animation

#### **Rate Expansion** (0-60px)  
- Based on speech rate/tempo
- Faster speech = more dynamic movement
- Controls particle generation rate

**Total Expansion Range**: 280px (base) to 570px (maximum)

### 3. **Synchronized Particle Properties**

#### **Particle Generation Rate**
```
baseParticles + (audioIntensity × 12)
```
- Ready: 8-12 particles/frame
- Listening: 12-24 particles/frame
- Speaking: 16-32 particles/frame
- Processing: 10-22 particles/frame

#### **Particle Speed**
```
baseSpeed × (1 + rate × 2.5 + pitch × 1.5)
```
- Particles move faster during high-pitched, fast speech
- Creates explosive outward motion during speech peaks

#### **Particle Lifecycle**
- **Attack**: 30-50ms (faster with high speech rate)
- **Hold**: 50-80ms (longer with high volume)
- **Decay**: 70-100ms (faster with high pitch)
- **Stuck Time**: 10-110ms (adaptive based on audio)

### 4. **Natural Speech Simulation**

#### **Speech Rhythm Pattern**
- **Base Volume**: 0.4 + sine wave (0.8 phase) × 0.15
- **Volume Variation**: +25% random
- **Update Rate**: Every 80ms (natural speech rhythm)

#### **Pitch Melody**
- **Base Pitch**: 0.5 + sine wave (0.6 phase) × 0.2
- **Pitch Variation**: +15% random
- **Follows Natural Intonation**: Rises and falls like real speech

#### **Speech Rate Fluctuation**
- **Base Rate**: 0.6 + cosine wave (0.7 phase) × 0.15
- **Rate Variation**: +20% random
- **Occasional Pauses**: 5% probability (30% volume, 40% rate)

#### **Word Boundary Events**
- Volume boost on word start (+10%)
- Slight pitch variation (±5%)
- Creates natural speech cadence

### 5. **Smooth State Transitions**

#### **Ready State (Idle Breathing)**
```javascript
Volume: 0.08 + sin(phase × 0.8) × 0.06
Pitch:  0.12 + sin(phase × 1.2) × 0.08  
Rate:   0.1 + cos(phase × 0.6) × 0.05
```
- Gentle breathing pattern
- Multiple sine waves for organic motion
- Phase increment: 0.02/frame

#### **Processing State (Pulsing)**
```javascript
3 overlapping sine waves:
- Pulse1: sin(phase × 1.2) × 0.15
- Pulse2: sin(phase × 2.3) × 0.1
- Pulse3: cos(phase × 0.8) × 0.12
```
- Complex organic pulsing
- Non-repeating pattern feel
- Phase increment: 0.05/frame

#### **Listening State**
- Real-time microphone analysis
- Direct FFT frequency data
- Immediate response to voice input

#### **Speaking State**
- Simulated natural speech
- Smooth fade-out over 1 second
- Ease-out curve for natural ending

### 6. **Visual Enhancements**

#### **Dynamic Particle Size**
```
baseSize × (1 + volume × 0.5 + pitch × 0.3)
```
- Particles grow during speech
- Size range: 2.5px to 5.5px

#### **Glow Effect**
- Activated when: volume > 0.3 OR pitch > 0.4
- Glow radius: 2.5× particle size
- Opacity: (volume + pitch) × 0.15
- Creates energy burst effect

#### **Rotation Speed**
```
baseRotation × (1 + rate × 1.5 + pitch × 0.8)
```
- Sphere spins faster during active speech
- Adds kinetic energy to animation

### 7. **Fade Transitions**

#### **Fade to Idle**
- Exponential decay (85% per step)
- 20 steps over 1 second
- Smooth transition to breathing

#### **Fade from Speaking**
- Ease-out curve
- 20 steps over 1 second  
- Natural speech ending feel

## State Configurations

| State | Base Size | Particles/Frame | Rotation | Speed |
|-------|-----------|-----------------|----------|-------|
| **Ready** | 280px | 8 | Slow | 0.002 |
| **Listening** | 320px | 12 | Medium | 0.003 |
| **Speaking** | 380px | 16 | Fast | 0.004 |
| **Processing** | 300px | 10 | Medium-Slow | 0.0025 |

## Animation Timing

- **Main Loop**: 10/24 ms (~41.6 FPS)
- **Audio Analysis**: Every 50ms (20 FPS)
- **Speech Simulation**: Every 80ms (12.5 FPS)
- **Smooth Interpolation**: Every frame (41.6 FPS)

## Audio Metrics

### **Volume** (0-1)
- Calculated from FFT amplitude average
- Affects: sphere size, particle count, particle size

### **Pitch** (0-1)
- Dominant frequency detection
- Affects: expansion height, particle speed, decay rate

### **Rate** (0-1)
- High/low frequency energy ratio
- Affects: rotation speed, particle velocity, generation rate

## Performance Optimizations

1. **Particle Recycling**: Reuse particle objects
2. **Smooth Interpolation**: Prevents jitter
3. **Conditional Rendering**: Glow only when needed
4. **Efficient FFT**: 2048 bins, analyzed every 50ms
5. **State-based Updates**: Different update rates per state

## User Experience

### **Visual Feedback**
- 🔵 **Blue Sphere**: AI is ready and breathing
- 🟢 **Green Sphere**: Listening to your voice (expands with speech)
- 🟠 **Orange Sphere**: AI is speaking (pulsing with speech rhythm)
- 🟣 **Purple Sphere**: Processing your request (gentle pulsing)

### **Expansion Behavior**
- **Quiet Speech**: Small gentle expansion
- **Normal Speech**: Medium expansion with rhythm
- **Loud Speech**: Large explosive expansion
- **High Pitch**: Taller, more vertical expansion
- **Fast Speech**: Rapid pulsing and rotation

### **Smooth Transitions**
- No sudden jumps in size
- Gradual color transitions
- Natural fade in/out
- Organic motion feel

## Technical Implementation

### **Interpolation Formula**
```javascript
current += (target - current) × smoothingFactor
```
- Exponential approach to target
- Automatic deceleration near target
- Prevents overshooting

### **Expansion Calculation**
```javascript
targetSize = baseSize + 
             (volume × 150) + 
             (pitch × 80) + 
             (rate × 60)
```

### **Particle Velocity**
```javascript
speed = baseSpeed × (1 + rate × 2.5 + pitch × 1.5)
```

## Browser Compatibility
- ✅ Chrome/Edge (Full Web Audio API support)
- ✅ Firefox (Full support)
- ⚠️ Safari (Limited Web Audio API)
- ✅ Mobile Chrome/Edge (Touch + mic support)

## Future Enhancements
- [ ] Stereo positioning based on pitch
- [ ] Particle color shifts with emotion
- [ ] Harmonic frequency visualization
- [ ] Custom particle shapes per state
- [ ] WebGL acceleration for more particles
