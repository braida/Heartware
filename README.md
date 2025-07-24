Emotionally Responsible Recommender System
Author: Naima Bouri

Abstract
This paper introduces a novel approach to recommendation systems that prioritizes user well-being.
By leveraging sentiment analysis to track users' emotional states across interactions, the system
adapts recommendations to avoid emotional degradation and encourage positive affect. This model treats well-being not as a static user state but as a dynamic feedback loop shaped by algorithmic
interactions. We propose a mechanism that measures the emotional delta between the end of one interaction and the start of the next, and uses this data to steer future recommendations. This
emotionally responsible framework opens a new path for designing tech that prioritizes long-term
human flourishing.

1. Introduction
Recommendation systems have traditionally prioritized engagement metrics such as click-through
rates, session duration, and return visits. While effective for growth, these metrics can contribute to
emotional harm through addiction, polarization, and negative affect reinforcement. This paper
proposes an alternative: a recommender system optimized for emotional sustainability.

2. Modeling Emotional Feedback
With tracking emotional states using sentiment analysis at the end of each session.
This sentiment is logged and later compared to the emotional tone of the user's next return. The
difference forms a feedback signal, which the model uses to adjust content weighting in future recommendations.

3. Implementation
The implementation includes three core components: 1) a sentiment classifier for post-session analysis, 2) a feedback mechanism comparing previous emotional states, and 3) a recommendation
logic that rebalances content based on well-being improvements. This structure allows the model to avoid patterns associated with negative cycles.

4. Use Case: Social Media Platforme
We apply this model to a simulated Twitter environment, using historical tweets and engagement data to identify how well-being-aware recommendations change user trajectories. The model aims to prevent depressive spirals and introduce supportive, emotionally neutral or uplifting content based on recent sentiment patterns.

5. Conclusion
An emotionally responsible recommender system can significantly reshape how digital platforms interact with users. By prioritizing psychological sustainability, we pave the way for ethical,
human-centered AI systems that serve not only attention but flourishing.
